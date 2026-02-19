from typing import Dict, NamedTuple, Optional

from BaseClasses import Location
from .Names import LocationName, RegionName


astronautilus_base_id: int = 0x7F0000


class AstronautilusLocation(Location):
    game = "Celeste 64"


class AstronautilusLocationData(NamedTuple):
    region: str
    address: Optional[int] = None


strawberry_location_data_table: Dict[str, AstronautilusLocationData] = {
    LocationName.shop1_item1:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x00),
    LocationName.shop1_item2:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x01),
    LocationName.shop1_item3:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x02),
    LocationName.shop1_item4:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x03),
    LocationName.shop1_item5:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x04),
    LocationName.shop1_item6:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x05),
    LocationName.shop1_item7:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x06),
    LocationName.shop1_item8:  AstronautilusLocationData(RegionName.shop_1,        astronautilus_base_id + 0x07),
    #0x1D
}

friend_location_data_table: Dict[str, AstronautilusLocationData] = {
    LocationName.granny_1:   AstronautilusLocationData(RegionName.granny_island,   astronautilus_base_id + 0x100 + 0x00),
    LocationName.granny_2:   AstronautilusLocationData(RegionName.granny_island,   astronautilus_base_id + 0x100 + 0x01),
    LocationName.granny_3:   AstronautilusLocationData(RegionName.granny_island,   astronautilus_base_id + 0x100 + 0x02),
    LocationName.theo_1:     AstronautilusLocationData(RegionName.granny_island,   astronautilus_base_id + 0x100 + 0x03),
    LocationName.theo_2:     AstronautilusLocationData(RegionName.granny_island,   astronautilus_base_id + 0x100 + 0x04),
    LocationName.theo_3:     AstronautilusLocationData(RegionName.granny_island,   astronautilus_base_id + 0x100 + 0x05),
    LocationName.badeline_1: AstronautilusLocationData(RegionName.badeline_island, astronautilus_base_id + 0x100 + 0x06),
    LocationName.badeline_2: AstronautilusLocationData(RegionName.badeline_island, astronautilus_base_id + 0x100 + 0x07),
    LocationName.badeline_3: AstronautilusLocationData(RegionName.badeline_island, astronautilus_base_id + 0x100 + 0x08),
}

sign_location_data_table: Dict[str, AstronautilusLocationData] = {
    LocationName.sign_1: AstronautilusLocationData(RegionName.granny_island,   astronautilus_base_id + 0x200 + 0x00),
    LocationName.sign_2: AstronautilusLocationData(RegionName.granny_island,   astronautilus_base_id + 0x200 + 0x01),
    LocationName.sign_3: AstronautilusLocationData(RegionName.highway_island,  astronautilus_base_id + 0x200 + 0x02),
    LocationName.sign_4: AstronautilusLocationData(RegionName.se_house_island, astronautilus_base_id + 0x200 + 0x03),
    LocationName.sign_5: AstronautilusLocationData(RegionName.badeline_island, astronautilus_base_id + 0x200 + 0x04),
}

car_location_data_table: Dict[str, AstronautilusLocationData] = {
    LocationName.car_1: AstronautilusLocationData(RegionName.intro_islands, astronautilus_base_id + 0x300 + 0x00),
    LocationName.car_2: AstronautilusLocationData(RegionName.granny_island, astronautilus_base_id + 0x300 + 0x01),
}

world_location_data_table: Dict[str, AstronautilusLocationData] = {
    LocationName.world_1:  AstronautilusLocationData(RegionName.world_1,    astronautilus_base_id + 0x400 + 0x00),
    LocationName.world_2:  AstronautilusLocationData(RegionName.world_2,    astronautilus_base_id + 0x400 + 0x01),
    LocationName.world_3:  AstronautilusLocationData(RegionName.world_3,    astronautilus_base_id + 0x400 + 0x02),
    LocationName.world_4:  AstronautilusLocationData(RegionName.world_4,    astronautilus_base_id + 0x400 + 0x03),
    LocationName.world_5:  AstronautilusLocationData(RegionName.world_5,    astronautilus_base_id + 0x400 + 0x04),
}

location_data_table: Dict[str, AstronautilusLocationData] = {**strawberry_location_data_table,
                                                         **friend_location_data_table,
                                                         **sign_location_data_table,
                                                         **car_location_data_table,
                                                         **checkpoint_location_data_table}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
