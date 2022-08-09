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
    command_parser = CommandParser()
    dungeon = Dungeon("data/dungeons/level1.dng")
    dungeon_window = display.create_window(5, 5, 20, 20)
    player = Player(3, 5, "*")

    dungeon.add_object(player)
    dungeon.draw(display, dungeon_window)

    display.refresh()
    display.debug_message("hello world")
    time.sleep(3)

if(__name__ == "__main__"):
    main(display=Display)
