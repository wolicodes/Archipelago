from worlds.LauncherComponents import Component, Type, components, launch


def run_client(*args: str) -> None:
    from .client import launch_desvelado_client
    launch(launch_desvelado_client, name="Desvelado Client", args=args)


components.append(
    Component(
        "Desvelado Client",
        func=run_client,
        game_name="Desvelado",
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)
