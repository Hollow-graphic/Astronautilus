from typing import Dict, NamedTuple, Optional

from BaseClasses import Location
from .Names import LocationName, RegionName


astronautilus_base_id: int = 0x7F0000


class AstronautilusLocation(Location):
    game = "Celeste 64"


class AstronautilusLocationData(NamedTuple):
    region: str
    address: Optional[int] = None


shop1_item_location_data_table: Dict[str, AstronautilusLocationData] = {
    LocationName.shop1_item1:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x10),
    LocationName.shop1_item2:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x11),
    LocationName.shop1_item3:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x12),
    LocationName.shop1_item4:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x13),
    LocationName.shop1_item5:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x14),
    LocationName.shop1_item6:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x15),
    LocationName.shop1_item7:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x16),
    LocationName.shop1_item8:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x17),
}
shop2_item_location_data_table: Dict[str, AstronautilusLocationData] = {
    LocationName.shop2_item1:  AstronautilusLocationData(RegionName.shop_2,        astronautilus_base_id + 0x20),
    LocationName.shop2_item2:  AstronautilusLocationData(RegionName.shop_2,        astronautilus_base_id + 0x21),
    LocationName.shop2_item3:  AstronautilusLocationData(RegionName.shop_2,        astronautilus_base_id + 0x22),
    LocationName.shop2_item4:  AstronautilusLocationData(RegionName.shop_2,        astronautilus_base_id + 0x23),
    LocationName.shop2_item5:  AstronautilusLocationData(RegionName.shop_2,        astronautilus_base_id + 0x24),
    LocationName.shop2_item6:  AstronautilusLocationData(RegionName.shop_2,        astronautilus_base_id + 0x25),
    LocationName.shop2_item7:  AstronautilusLocationData(RegionName.shop_2,        astronautilus_base_id + 0x26),
    LocationName.shop2_item8:  AstronautilusLocationData(RegionName.shop_2,        astronautilus_base_id + 0x27),
}
shop3_item_location_data_table: Dict[str, AstronautilusLocationData] = {
    LocationName.shop3_item1:  AstronautilusLocationData(RegionName.shop_3,        astronautilus_base_id + 0x30),
    LocationName.shop3_item2:  AstronautilusLocationData(RegionName.shop_3,        astronautilus_base_id + 0x31),
    LocationName.shop3_item3:  AstronautilusLocationData(RegionName.shop_3,        astronautilus_base_id + 0x32),
    LocationName.shop3_item4:  AstronautilusLocationData(RegionName.shop_3,        astronautilus_base_id + 0x33),
    LocationName.shop3_item5:  AstronautilusLocationData(RegionName.shop_3,        astronautilus_base_id + 0x34),
    LocationName.shop3_item6:  AstronautilusLocationData(RegionName.shop_3,        astronautilus_base_id + 0x35),
    LocationName.shop3_item7:  AstronautilusLocationData(RegionName.shop_3,        astronautilus_base_id + 0x36),
    LocationName.shop3_item8:  AstronautilusLocationData(RegionName.shop_3,        astronautilus_base_id + 0x37),
}
shop4_item_location_data_table: Dict[str, AstronautilusLocationData] = {
    LocationName.shop4_item1:  AstronautilusLocationData(RegionName.shop_4,        astronautilus_base_id + 0x40),
    LocationName.shop4_item2:  AstronautilusLocationData(RegionName.shop_4,        astronautilus_base_id + 0x41),
    LocationName.shop4_item3:  AstronautilusLocationData(RegionName.shop_4,        astronautilus_base_id + 0x42),
    LocationName.shop4_item4:  AstronautilusLocationData(RegionName.shop_4,        astronautilus_base_id + 0x43),
    LocationName.shop4_item5:  AstronautilusLocationData(RegionName.shop_4,        astronautilus_base_id + 0x44),
    LocationName.shop4_item6:  AstronautilusLocationData(RegionName.shop_4,        astronautilus_base_id + 0x45),
    LocationName.shop4_item7:  AstronautilusLocationData(RegionName.shop_4,        astronautilus_base_id + 0x46),
    LocationName.shop4_item8:  AstronautilusLocationData(RegionName.shop_4,        astronautilus_base_id + 0x47),
}
shop5_item_location_data_table: Dict[str, AstronautilusLocationData] = {
    LocationName.shop5_item1:  AstronautilusLocationData(RegionName.shop_5,        astronautilus_base_id + 0x50),
    LocationName.shop5_item2:  AstronautilusLocationData(RegionName.shop_5,        astronautilus_base_id + 0x51),
    LocationName.shop5_item3:  AstronautilusLocationData(RegionName.shop_5,        astronautilus_base_id + 0x52),
    LocationName.shop5_item4:  AstronautilusLocationData(RegionName.shop_5,        astronautilus_base_id + 0x53),
    LocationName.shop5_item5:  AstronautilusLocationData(RegionName.shop_5,        astronautilus_base_id + 0x54),
    LocationName.shop5_item6:  AstronautilusLocationData(RegionName.shop_5,        astronautilus_base_id + 0x55),
    LocationName.shop5_item7:  AstronautilusLocationData(RegionName.shop_5,        astronautilus_base_id + 0x56),
    LocationName.shop5_item8:  AstronautilusLocationData(RegionName.shop_5,        astronautilus_base_id + 0x57),
}

world_location_data_table: Dict[str, AstronautilusLocationData] = {
    LocationName.world_1:  AstronautilusLocationData(RegionName.world_1,    astronautilus_base_id + 0x100 + 0x00),
    LocationName.world_2:  AstronautilusLocationData(RegionName.world_2,    astronautilus_base_id + 0x100 + 0x01),
    LocationName.world_3:  AstronautilusLocationData(RegionName.world_3,    astronautilus_base_id + 0x100 + 0x02),
    LocationName.world_4:  AstronautilusLocationData(RegionName.world_4,    astronautilus_base_id + 0x100 + 0x03),
    LocationName.world_5:  AstronautilusLocationData(RegionName.world_5,    astronautilus_base_id + 0x100 + 0x04),
}

location_data_table: Dict[str, AstronautilusLocationData] = {**shop1_item_location_data_table,
                                                         **shop2_item_location_data_table,
                                                         **shop3_item_location_data_table,
                                                         **shop4_item_location_data_table,
                                                         **shop5_item_location_data_table,
                                                         **world_location_data_table}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
