#!python3

from models.command_parser import CommandParser
from models.monster import MonsterFactory
from models.dungeon import Dungeon
from models.player import Player
from models.hud import Hud
from models.display import Display
from models.display import display_decorator

import time

def keyboard_handler(key):
    pass

@display_decorator
def main(display):
    player = Player(3, 5, "PL")
    dungeon = Dungeon("data/dungeons/level1.dng")
    dungeon.add_object(player)

    hud = Hud(display, keyboard_handler)
    hud.set_dungeon(dungeon)
    hud.start_keyboard()

if(__name__ == "__main__"):
    main(display=Display)
