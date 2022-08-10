#!python3

from models.command_parser import CommandParser
from models.monster import MonsterFactory
from models.dungeon import Dungeon
from models.player import Player
from models.display import Display
from models.display import display_decorator

import time

@display_decorator
def main(display):
    dungeon = Dungeon("data/dungeons/level1.dng")
    dungeon_window = display.create_pad(10, 10, 100, 100, 7, 14)
    player = Player(3, 5, "*")

    dungeon.add_object(player)
    dungeon.draw(display, dungeon_window)

    display.debug_message("hello world")
    display.refresh()
    display.wait()

if(__name__ == "__main__"):
    main(display=Display)
