#!python3

from models.hud import Hud
from models.display import Display
from models.display import display_decorator
from models.logger import Logger
from models.game import Game

import time

@display_decorator
def main(display):
    game = Game()

    hud = Hud(display, game.input_handler)
    hud.set_dungeon(game.dungeon)
    hud.start_keyboard()

if(__name__ == "__main__"):
    main(display=Display)
