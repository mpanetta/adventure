from models.logger import Logger

class CommandParser:
    KEY_H = "h"
    KEY_J = "j"
    KEY_K = "k"
    KEY_L = "l"
    KEY_Q = "q"

    COMMAND_LEFT = "left"
    COMMAND_RIGHT = "right"
    COMMAND_UP = "up"
    COMMAND_DOWN = "down"
    COMMAND_QUIT = "quit"
    COMMAND_HELP = "Help"

    def parse(self, input_string):
        Logger.log(f"command buffer: {input_string}")
        if(input_string == CommandParser.KEY_H): return CommandParser.COMMAND_LEFT
        if(input_string == CommandParser.KEY_L): return CommandParser.COMMAND_RIGHT
        if(input_string == CommandParser.KEY_K): return CommandParser.COMMAND_UP
        if(input_string == CommandParser.KEY_J): return CommandParser.COMMAND_DOWN
        if(input_string == CommandParser.KEY_Q): return CommandParser.COMMAND_QUIT

        return None

    # private functions

    def _match_key(input_strings, *args):
        for arg in args:
            if(arg == input_string): return True
        return False
