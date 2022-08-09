class CommandParser:
    KEY_G = "g"
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
        if(input_string == KEY_G): return COMMAND_LEFT
        if(input_string == KEY_L): return COMMAND_RIGHT
        if(input_string == KEY_H): return COMMAND_UP
        if(input_string == KEY_J): return COMMAND_DOWN
        if(input_string == KEY_Q): return COMMAND_QUIT

        return COMMAND_HELP

    # private functions

    def _match_key(input_strings, *args):
        for arg in args:
            if(arg == input_string): return True
        return False
