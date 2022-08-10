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
    keyboard_args = { "display": display }
    hud = Hud(display, keyboard_handler)
    hud.start_keyboard()

    # hud.wait()
    # dungeon = Dungeon("data/dungeons/level1.dng")
    # dungeon_window = display.create_pad(0, 2, 100, 100, 7, 14)
    # player = Player(3, 5, "*")
    #
    # dungeon.add_object(player)
    # dungeon.draw(display, dungeon_window)
    #
    # display.debug_message("hello world")
    # display.refresh()
    # display.wait()
    # display.end()
    #
if(__name__ == "__main__"):
    main(display=Display)
