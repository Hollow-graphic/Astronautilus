from typing import Dict, List, Tuple, Callable

from BaseClasses import CollectionState, Region
from worlds.generic.Rules import set_rule

from . import Celeste64World
from .Names import ItemName, LocationName, RegionName


def set_rules(world: AstronautilusWorld):
    if world.options.logic_difficulty == "standard":
        world.active_logic_mapping = location_standard_moves_logic
        world.active_region_logic_mapping = region_standard_moves_logic
    else:
        world.active_logic_mapping = location_hard_moves_logic
        world.active_region_logic_mapping = region_hard_moves_logic

    for location in world.multiworld.get_locations(world.player):
        set_rule(location, lambda state, location=location: location_rule(state, world, location.name))

    # Completion condition.
    world.multiworld.completion_condition[world.player] = lambda state: goal_rule(state, world)


location_logic: Dict[str, List[List[str]]] = {
    LocationName.shop1_item1: [[ItemName.shopdiscount1]],
    LocationName.shop1_item2: [[ItemName.shopdiscount1]],
    LocationName.shop1_item3: [[ItemName.shopdiscount1]],
    LocationName.shop1_item4: [[ItemName.shopdiscount1]],
    LocationName.shop1_item5: [[ItemName.shopdiscount1]],
    LocationName.shop1_item6: [[ItemName.shopdiscount1]],
    LocationName.shop1_item7: [[ItemName.shopdiscount1]],
    LocationName.shop1_item8: [[ItemName.shopdiscount1]],

    LocationName.shop2_item1: [[ItemName.shopdiscount2]],
    LocationName.shop2_item2: [[ItemName.shopdiscount2]],
    LocationName.shop2_item3: [[ItemName.shopdiscount2]],
    LocationName.shop2_item4: [[ItemName.shopdiscount2]],
    LocationName.shop2_item5: [[ItemName.shopdiscount2]],
    LocationName.shop2_item6: [[ItemName.shopdiscount2]],
    LocationName.shop2_item7: [[ItemName.shopdiscount2]],
    LocationName.shop2_item8: [[ItemName.shopdiscount2]],

    LocationName.shop3_item1: [[ItemName.shopdiscount3]],
    LocationName.shop3_item2: [[ItemName.shopdiscount3]],
    LocationName.shop3_item3: [[ItemName.shopdiscount3]],
    LocationName.shop3_item4: [[ItemName.shopdiscount3]],
    LocationName.shop3_item5: [[ItemName.shopdiscount3]],
    LocationName.shop3_item6: [[ItemName.shopdiscount3]],
    LocationName.shop3_item7: [[ItemName.shopdiscount3]],
    LocationName.shop3_item8: [[ItemName.shopdiscount3]],

    LocationName.shop4_item1: [[ItemName.shopdiscount4]],
    LocationName.shop4_item2: [[ItemName.shopdiscount4]],
    LocationName.shop4_item3: [[ItemName.shopdiscount4]],
    LocationName.shop4_item4: [[ItemName.shopdiscount4]],
    LocationName.shop4_item5: [[ItemName.shopdiscount4]],
    LocationName.shop4_item6: [[ItemName.shopdiscount4]],
    LocationName.shop4_item7: [[ItemName.shopdiscount4]],
    LocationName.shop4_item8: [[ItemName.shopdiscount4]],

    LocationName.shop5_item1: [[ItemName.shopdiscount5]],
    LocationName.shop5_item2: [[ItemName.shopdiscount5]],
    LocationName.shop5_item3: [[ItemName.shopdiscount5]],
    LocationName.shop5_item4: [[ItemName.shopdiscount5]],
    LocationName.shop5_item5: [[ItemName.shopdiscount5]],
    LocationName.shop5_item6: [[ItemName.shopdiscount5]],
    LocationName.shop5_item7: [[ItemName.shopdiscount5]],
    LocationName.shop5_item8: [[ItemName.shopdiscount5]],
}

def location_rule(state: CollectionState, world: Celeste64World, loc: str) -> bool:
    if loc not in world.active_logic_mapping:
        return True

    for possible_access in world.active_logic_mapping[loc]:
        if state.has_all(possible_access, world.player):
            return True

    return False

def region_connection_rule(state: CollectionState, world: Celeste64World, region_connection: Tuple[str]) -> bool:
    if region_connection not in world.active_region_logic_mapping:
        return True

    for possible_access in world.active_region_logic_mapping[region_connection]:
        if state.has_all(possible_access, world.player):
            return True

    return False

def goal_rule(state: CollectionState, world: Celeste64World) -> bool:
    if not state.has(ItemName.strawberry, world.player, world.strawberries_required):
        return False

    goal_region: Region = world.multiworld.get_region(RegionName.badeline_island, world.player)
    return state.can_reach(goal_region)

def connect_region(world: Celeste64World, region: Region, dest_regions: List[str]):
    rules: Dict[str, Callable[[CollectionState], bool]] = {}

    for dest_region in dest_regions:
        region_connection: Tuple[str] = (region.name, dest_region)
        rules[dest_region] = lambda state, region_connection=region_connection: region_connection_rule(state, world, region_connection)

    region.add_exits(dest_regions, rules)
