from models.logger import Logger

class LeftCommand:
    def execute(self, game):
        row = game.player.row
        col = game.player.column - 1

        Logger.log(f"player: ({game.player.row}, {game.player.column})")        
        if(game.dungeon.is_passable(row, col)):
            game.player.column -= 1
