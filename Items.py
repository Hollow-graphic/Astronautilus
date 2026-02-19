from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Names import ItemName


astronautilus_base_id: int = 0xCA0000


class AstronautilusItem(Item):
    game = "Astronautilus"


class AstronautilusItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler


collectable_item_data_table: Dict[str, AstronautilusItemData] = {
    ItemName.shop_item: AstronautilusItemData(astronautilus_base_id + 0x0, ItemClassification.progression_skip_balancing),
    ItemName.pearl:  AstronautilusItemData(astronautilus_base_id + 0x9, ItemClassification.filler),
}

achievement_item_data_table: Dict[str, AstronautilusItemData] = {
    ItemName.shopdiscount1:         AstronautilusItemData(astronautilus_base_id + 0x1, ItemClassification.progression),
    ItemName.shopdiscount2:         AstronautilusItemData(astronautilus_base_id + 0x2, ItemClassification.progression),
    ItemName.shopdiscount3:         AstronautilusItemData(astronautilus_base_id + 0x3, ItemClassification.progression),
    ItemName.shopdiscount4:         AstronautilusItemData(astronautilus_base_id + 0x4, ItemClassification.progression),
    ItemName.shopdiscount5:         AstronautilusItemData(astronautilus_base_id + 0x5, ItemClassification.progression),
}

move_item_data_table: Dict[str, AstronautilusItemData] = {
    ItemName.ground_dash: AstronautilusItemData(astronautilus_base_id + 0xA, ItemClassification.progression),
    ItemName.air_dash:    AstronautilusItemData(astronautilus_base_id + 0xB, ItemClassification.progression),
    ItemName.skid_jump:   AstronautilusItemData(astronautilus_base_id + 0xC, ItemClassification.progression),
    ItemName.climb:       AstronautilusItemData(astronautilus_base_id + 0xD, ItemClassification.progression),
}

checkpoint_item_data_table: Dict[str, AstronautilusItemData] = {
    ItemName.checkpoint_1:  AstronautilusItemData(astronautilus_base_id + 0x20, ItemClassification.progression),
    ItemName.checkpoint_2:  AstronautilusItemData(astronautilus_base_id + 0x21, ItemClassification.progression),
    ItemName.checkpoint_3:  AstronautilusItemData(astronautilus_base_id + 0x22, ItemClassification.progression),
    ItemName.checkpoint_4:  AstronautilusItemData(astronautilus_base_id + 0x23, ItemClassification.progression),
    ItemName.checkpoint_5:  AstronautilusItemData(astronautilus_base_id + 0x24, ItemClassification.progression),
    ItemName.checkpoint_6:  AstronautilusItemData(astronautilus_base_id + 0x25, ItemClassification.progression),
    ItemName.checkpoint_7:  AstronautilusItemData(astronautilus_base_id + 0x26, ItemClassification.progression),
    ItemName.checkpoint_8:  AstronautilusItemData(astronautilus_base_id + 0x27, ItemClassification.progression),
    ItemName.checkpoint_9:  AstronautilusItemData(astronautilus_base_id + 0x28, ItemClassification.progression),
    ItemName.checkpoint_10: AstronautilusItemData(astronautilus_base_id + 0x29, ItemClassification.progression),
}

item_data_table: Dict[str, AstronautilusItemData] = {**collectable_item_data_table,
                                                 **unlockable_item_data_table,
                                                 **move_item_data_table,
                                                 **checkpoint_item_data_table}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
