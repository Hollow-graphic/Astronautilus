from typing import Dict, List, NamedTuple

from .Names import RegionName

class Astronautilus(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, Astronautilus] = {
    "Menu": Astronautilus([RegionName.World]),

    RegionName.World: Astronautilus([RegionName.level_1, RegionName.level_2, RegionName.level_3, RegionName.level_4, RegionName.level_5]),

    RegionName.level_1:              Astronautilus([RegionName.shop_1]),
    RegionName.level_2:              Astronautilus([RegionName.shop_2]),
    RegionName.level_3:              Astronautilus([RegionName.shop_3]),
    RegionName.level_4:              Astronautilus([RegionName.shop_4]),
    RegionName.level_5:              Astronautilus([RegionName.shop_5]),
}
