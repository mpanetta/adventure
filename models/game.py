from models.dungeon import Dungeon
from models.player import Player
from models.command_parser import CommandParser
from models.command_factory import CommandFactory

class Game:
    def __init__(self):
        self._create_initial_dungeon()
        self._create_player()
        self._create_command_parser()

    # properties

    @property
    def dungeon(self):
        return self._dungeon

    @property
    def player(self):
        return self._player
    
    # public methods

    def input_handler(self, text):
        command_class = self._command_parser.parse(text)
        if(command_class == None): return False

        command = CommandFactory.create_command(command_class)
        command.execute(self)
        return True
 
    # private methods

    def _create_initial_dungeon(self):
        self._dungeon = Dungeon("data/dungeons/level1.dng")

    def _create_player(self):
        self._player = Player(3, 5, "PL")
        self._dungeon.add_object(self._player)
        self._dungeon.set_camera_object(self._player)

    def _create_command_parser(self):
        self._command_parser = CommandParser()
