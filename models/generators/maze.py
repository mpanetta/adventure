import random

class Maze:
    def __init__(self, base_map):
        self._base_map = base_map

    # public methods

    def generate(self, row=None, column=None):
        if(row == None): row = random.randint(1, self._base_map.height - 1)
        if(column == None): col = random.randint(1, self._base_map.width - 1)
