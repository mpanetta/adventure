from models.logger import Logger

class UpCommand:
    def execute(self, game):
        row = game.player.row - 1
        col = game.player.column

        Logger.log(f"player: ({game.player.row}, {game.player.column})")        
        if(game.dungeon.is_passable(row, col)):
            game.player.row -= 1
