from typing import Dict, List, NamedTuple

from .Names import RegionName

class Astronautilus(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, Astronautilus] = {
    "Menu": Astronautilus([RegionName.World]),

    RegionName.World: Astronautilus([RegionName.world_1, RegionName.world_2, RegionName.world_3, RegionName.world_4, RegionName.world_5]),

    RegionName.world_1:              Astronautilus([RegionName.shop_1]),
    RegionName.world_2:              Astronautilus([RegionName.shop_2]),
    RegionName.world_3:              Astronautilus([RegionName.shop_3]),
    RegionName.world_4:              Astronautilus([RegionName.shop_4]),
    RegionName.world_5:              Astronautilus([RegionName.shop_5]),
}
