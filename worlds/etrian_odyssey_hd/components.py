from worlds.LauncherComponents import Component, Type, components
from worlds.etrian_odyssey_hd.cmd_gendb import gen_dyndb

components.append(
    Component(
        "Etrian Odyssey HD - Database Generator",
        func=gen_dyndb,
        game_name="Etrian Odyssey HD",
        component_type=Type.TOOL,
        supports_uri=False,
    )
)
