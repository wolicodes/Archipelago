from worlds.LauncherComponents import Component, Type, components, launch


def run_client(*args: str) -> None:
    from .client import run_as_goal_client
    launch(run_as_goal_client, name="GoalClient", args=args)


components.append(
    Component(
        "Goal Client",
        func=run_client,
        component_type=Type.CLIENT,
        description="Connect and send /goal to mark a slot as completed.",
    )
)
