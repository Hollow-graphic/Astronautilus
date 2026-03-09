from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Names import ItemName


astronautilus_base_id: int = 0xCA0000


class Astronautilus(Item):
    game = "Astronautilus"


class AstronautilusData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler


collectable_item_data_table: Dict[str, AstronautilusData] = {
    ItemName.strawberry: AstronautilusData(astronautilus_base_id + 0x0, ItemClassification.progression_skip_balancing),
    ItemName.raspberry:  AstronautilusData(astronautilus_base_id + 0x9, ItemClassification.filler),
}

unlockable_item_data_table: Dict[str, AstronautilusData] = {
    ItemName.dash_refill:        AstronautilusData(astronautilus_base_id + 0x1, ItemClassification.progression),
    ItemName.double_dash_refill: AstronautilusData(astronautilus_base_id + 0x2, ItemClassification.progression),
    ItemName.feather:            AstronautilusData(astronautilus_base_id + 0x3, ItemClassification.progression),
    ItemName.coin:               AstronautilusData(astronautilus_base_id + 0x4, ItemClassification.progression),
    ItemName.cassette:           AstronautilusData(astronautilus_base_id + 0x5, ItemClassification.progression),
    ItemName.traffic_block:      AstronautilusData(astronautilus_base_id + 0x6, ItemClassification.progression),
    ItemName.spring:             AstronautilusData(astronautilus_base_id + 0x7, ItemClassification.progression),
    ItemName.breakables:         AstronautilusData(astronautilus_base_id + 0x8, ItemClassification.progression),
}

move_item_data_table: Dict[str, AstronautilusData] = {
    ItemName.ground_dash: AstronautilusData(astronautilus_base_id + 0xA, ItemClassification.progression),
    ItemName.air_dash:    AstronautilusData(astronautilus_base_id + 0xB, ItemClassification.progression),
    ItemName.skid_jump:   AstronautilusData(astronautilus_base_id + 0xC, ItemClassification.progression),
    ItemName.climb:       AstronautilusData(astronautilus_base_id + 0xD, ItemClassification.progression),
}

checkpoint_item_data_table: Dict[str, AstronautilusData] = {
    ItemName.checkpoint_1:  AstronautilusData(astronautilus_base_id + 0x20, ItemClassification.progression),
    ItemName.checkpoint_2:  AstronautilusData(astronautilus_base_id + 0x21, ItemClassification.progression),
    ItemName.checkpoint_3:  AstronautilusData(astronautilus_base_id + 0x22, ItemClassification.progression),
    ItemName.checkpoint_4:  AstronautilusData(astronautilus_base_id + 0x23, ItemClassification.progression),
    ItemName.checkpoint_5:  AstronautilusData(astronautilus_base_id + 0x24, ItemClassification.progression),
    ItemName.checkpoint_6:  AstronautilusData(astronautilus_base_id + 0x25, ItemClassification.progression),
    ItemName.checkpoint_7:  AstronautilusData(astronautilus_base_id + 0x26, ItemClassification.progression),
    ItemName.checkpoint_8:  AstronautilusData(astronautilus_base_id + 0x27, ItemClassification.progression),
    ItemName.checkpoint_9:  AstronautilusData(astronautilus_base_id + 0x28, ItemClassification.progression),
    ItemName.checkpoint_10: AstronautilusData(astronautilus_base_id + 0x29, ItemClassification.progression),
}

trap_item_data_table: Dict[str, AstronautilusData] = {
    ItemName.bald_trap:       AstronautilusData(astronautilus_base_id + 0x30, ItemClassification.trap),
    ItemName.bubble_trap:     AstronautilusData(astronautilus_base_id + 0x31, ItemClassification.trap),
    ItemName.hiccup_trap:     AstronautilusData(astronautilus_base_id + 0x32, ItemClassification.trap),
    ItemName.ice_trap:        AstronautilusData(astronautilus_base_id + 0x33, ItemClassification.trap),
    ItemName.invisible_trap:  AstronautilusData(astronautilus_base_id + 0x34, ItemClassification.trap),
    ItemName.literature_trap: AstronautilusData(astronautilus_base_id + 0x35, ItemClassification.trap),
    ItemName.reverse_trap:    AstronautilusData(astronautilus_base_id + 0x36, ItemClassification.trap),
    ItemName.stun_trap:       AstronautilusData(astronautilus_base_id + 0x37, ItemClassification.trap),
    ItemName.zoom_in_trap:    AstronautilusData(astronautilus_base_id + 0x38, ItemClassification.trap),
    ItemName.zoom_out_trap:   AstronautilusData(astronautilus_base_id + 0x39, ItemClassification.trap),
}

discount_item_data_table: Dict[str, AstronautilusData] = {
    ItemName.discount_1:     AstronautilusData(astronautilus_base_id + 0x40, ItemClassification.trap),
    ItemName.discount_2:     AstronautilusData(astronautilus_base_id + 0x41, ItemClassification.trap),
    ItemName.discount_3:     AstronautilusData(astronautilus_base_id + 0x42, ItemClassification.trap),
    ItemName.discount_4:     AstronautilusData(astronautilus_base_id + 0x43, ItemClassification.trap),
    ItemName.discount_5:     AstronautilusData(astronautilus_base_id + 0x44, ItemClassification.trap)
}

item_data_table: Dict[str, AstronautilusData] = {**collectable_item_data_table,
                                                 **unlockable_item_data_table,
                                                 **move_item_data_table,
                                                 **checkpoint_item_data_table,
                                                 **trap_item_data_table,
                                                 **discount_item_data_table}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
