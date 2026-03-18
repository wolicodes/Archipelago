from __future__ import annotations

import asyncio
import logging
import sys

from CommonClient import (
    CommonContext, ClientCommandProcessor, server_loop, gui_enabled, get_base_parser, handle_url_arg,
)
from NetUtils import ClientStatus
from Utils import async_start


logger = logging.getLogger("Client")


class GoalClientCommandProcessor(ClientCommandProcessor):
    ctx: GoalClientContext

    def _cmd_goal(self) -> bool:
        """Send goal completion to the server for the connected slot."""
        if not self.ctx.server or not self.ctx.slot:
            self.output("You must be connected to a server first.")
            return False
        if self.ctx.finished_game:
            self.output("Goal already sent for this slot.")
            return False
        async_start(self.ctx.send_goal())
        return True


class GoalClientContext(CommonContext):
    tags = CommonContext.tags | {"TextOnly"}
    game = ""
    items_handling = 0b111
    want_slot_data = False
    command_processor = GoalClientCommandProcessor

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game="")

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game
            # Query whether this slot already has goal completed
            self._status_key = f"_read_client_status_{self.team}_{self.slot}"
            async_start(self.send_msgs([{"cmd": "Get", "keys": [self._status_key]}]))
        elif cmd == "Retrieved":
            if hasattr(self, "_status_key") and self._status_key in args.get("keys", {}):
                if args["keys"][self._status_key] == ClientStatus.CLIENT_GOAL:
                    self.finished_game = True
                    logger.info("This slot has already completed its goal.")

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.game = ""
        self.finished_game = False
        await super().disconnect(allow_autoreconnect)

    async def send_goal(self):
        # Temporarily drop TextOnly so the server accepts the StatusUpdate
        self.tags = self.tags - {"TextOnly"}
        await self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}])
        await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
        self.finished_game = True
        # Restore TextOnly tag
        self.tags = self.tags | {"TextOnly"}
        await self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}])
        logger.info("Goal sent successfully!")


def run_as_goal_client(*args):
    async def main(args):
        ctx = GoalClientContext(args.connect, args.password)
        ctx.auth = args.name
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Archipelago Goal Client — connect and send /goal to complete.")
    parser.add_argument("--name", default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")
    args = parser.parse_args(args)

    args = handle_url_arg(args, parser=parser)

    colorama.just_fix_windows_console()
    asyncio.run(main(args))
    colorama.deinit()


if __name__ == "__main__":
    import ModuleUpdate
    ModuleUpdate.update()
    import Utils
    Utils.init_logging("GoalClient", exception_logger="Client")
    logging.getLogger().setLevel(logging.INFO)
    run_as_goal_client(*sys.argv[1:])
