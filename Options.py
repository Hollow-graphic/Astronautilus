from dataclasses import dataclass
import random

from Options import Choice, TextChoice, Range, Toggle, DeathLink, OptionGroup, PerGameCommonOptions, OptionError
from worlds.AutoWorld import World


class DeathLinkAmnesty(Range):
    """
    How many deaths it takes to send a DeathLink
    """
    display_name = "Death Link Amnesty"
    range_start = 1
    range_end = 5
    default = 1

class Auto-release(choice):
    """
    Does Auto-release when finishing the game
    """
    display_name = "Auto-release"
    option_activate = 0
    option_desactivate = 1
    default = 0


astronautilus_option_groups = [
    OptionGroup("Goal Options", [
        TotalStrawberries,
        StrawberriesRequiredPercentage,
    ]),
]


@dataclass
class Celeste64Options(PerGameCommonOptions):
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty

    auto_release: Auto-release


def resolve_options(world: World):
    # One Dash Hair
    if isinstance(world.options.madeline_one_dash_hair_color.value, str):
        try:
            world.madeline_one_dash_hair_color = int(world.options.madeline_one_dash_hair_color.value.strip("#")[:6], 16)
        except ValueError:
            raise OptionError(f"Invalid input for option `madeline_one_dash_hair_color`:"
                              f"{world.options.madeline_one_dash_hair_color.value} for "
                              f"{world.player_name}")
    elif world.options.madeline_one_dash_hair_color.value == ColorChoice.option_any_color:
        world.madeline_one_dash_hair_color = world.random.randint(0, 0xFFFFFF)
    else:
        world.madeline_one_dash_hair_color = world.options.madeline_one_dash_hair_color.value

    # Two Dash Hair
    if isinstance(world.options.madeline_two_dash_hair_color.value, str):
        try:
            world.madeline_two_dash_hair_color = int(world.options.madeline_two_dash_hair_color.value.strip("#")[:6], 16)
        except ValueError:
            raise OptionError(f"Invalid input for option `madeline_two_dash_hair_color`:"
                              f"{world.options.madeline_two_dash_hair_color.value} for "
                              f"{world.player_name}")
    elif world.options.madeline_two_dash_hair_color.value == ColorChoice.option_any_color:
        world.madeline_two_dash_hair_color = world.random.randint(0, 0xFFFFFF)
    else:
        world.madeline_two_dash_hair_color = world.options.madeline_two_dash_hair_color.value

    # No Dash Hair
    if isinstance(world.options.madeline_no_dash_hair_color.value, str):
        try:
            world.madeline_no_dash_hair_color = int(world.options.madeline_no_dash_hair_color.value.strip("#")[:6], 16)
        except ValueError:
            raise OptionError(f"Invalid input for option `madeline_no_dash_hair_color`:"
                              f"{world.options.madeline_no_dash_hair_color.value} for "
                              f"{world.player_name}")
    elif world.options.madeline_no_dash_hair_color.value == ColorChoice.option_any_color:
        world.madeline_no_dash_hair_color = world.random.randint(0, 0xFFFFFF)
    else:
        world.madeline_no_dash_hair_color = world.options.madeline_no_dash_hair_color.value

    # Feather Hair
    if isinstance(world.options.madeline_feather_hair_color.value, str):
        try:
            world.madeline_feather_hair_color = int(world.options.madeline_feather_hair_color.value.strip("#")[:6], 16)
        except ValueError:
            raise OptionError(f"Invalid input for option `madeline_feather_hair_color`:"
                              f"{world.options.madeline_feather_hair_color.value} for "
                              f"{world.player_name}")
    elif world.options.madeline_feather_hair_color.value == ColorChoice.option_any_color:
        world.madeline_feather_hair_color = world.random.randint(0, 0xFFFFFF)
    else:
        world.madeline_feather_hair_color = world.options.madeline_feather_hair_color.value

