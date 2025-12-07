from __future__ import annotations
from ..LauncherComponents import Component, components
from .data import items_constants as itm, locations_constants as loc
from .data import game_constants
from . import options
import json

def gen_dyndb():
    items = []
    tables = {}

    untreated = []

    for name, location in loc.LOCATION_DATA.items():
        table = ""
        id = 0
        locID = location.id
        items = []


        if name in game_constants.EVENT_DATA:
            table = "Flags"
            id = game_constants.EVENT_DATA[name]
            item = location.item is not None and itm.ITEM_NAME_TO_ID[location.item]
            if item is not None:
                items.append(item)

        # Shopsanity
        if location.flags == loc.EOHDFlag.SHOP:
            table = "Items"
            id = location.item is not None and itm.ITEM_NAME_TO_ID[location.item]
            items.append(id) # id is reward

        if table and id > 0 and locID > 0:
            if table not in tables:
                tables[table] = []

            tableRef = tables[table]
            entry = {
                "ID": id,
                "LocationName": name,
                "Location": locID,
                "Items": items
            }
            tableRef.append(entry)
        else:
            untreated.append(name)
            

    if len(untreated) > 0:
        print("some locations were not exported:")
        for loc_str in untreated:
            print(loc_str)

    dyndb = {"Tables": tables}
    with open('worlds/etrian_odyssey_hd/dyndb.json', 'w') as f:
        json.dump(dyndb, f, indent=2)