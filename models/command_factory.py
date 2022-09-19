import sys

from commands.quit_command import QuitCommand
from commands.left_command import LeftCommand
from commands.right_command import RightCommand
from commands.up_command import UpCommand
from commands.down_command import DownCommand

from models.logger import Logger

class _CommandFactory(object):
    _instance = None

    def __new__(klass):
        if(klass._instance == None):
            klass._instance = super(_CommandFactory, klass).__new__(klass)

            return klass._instance

    # public methods

    def create_command(self, command_class):
        Logger.log(f"command class: {command_class}")
        klass = self._constantize(f"{command_class.capitalize()}Command") 

        return klass()

    # private methods

    def _constantize(self, classname):
        return getattr(sys.modules[__name__], classname)

CommandFactory = _CommandFactory()
