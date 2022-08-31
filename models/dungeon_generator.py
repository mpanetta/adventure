from models.node import Node

import random
import string

ROCK_SYMBOL = "#"
SPACE_SYMBOL = " "
MIN_WIDTH = 4
MAX_WIDTH = 16
MIN_HEIGHT = 2
MAX_HEIGHT = 8

class DungeonGenerator:
    def __init__(self, height, width):
        self._root_node = Node(0, 0, height, width)
        self._map = self._generate_solid_dungeon(height, width)

        self._root_node.split()
        self._build_rooms()

    # public methods

    def draw(self):
        for row in self._map:
            for column in row:
                print(column, end="")
            print("\r")

    # private methods

    def _generate_solid_dungeon(self, height, width):
        dungeon = []

        for row in range(0, height):
            dungeon.append([])

            for col in range(0, width):
                dungeon[row].append(ROCK_SYMBOL)

        return dungeon

    def _build_rooms(self):
        for node in self._root_node.terminal_nodes():
            self._build_room(node)

    def _build_room(self, node):
        height = min(random.randint(MIN_HEIGHT, node.height - 2), MAX_HEIGHT)
        width = min(random.randint(MIN_WIDTH, node.width - 2), MAX_WIDTH)
        row = node.top_left.row + random.randint(1, node.height - height - 1)
        col = node.top_left.column  + random.randint(1, node.width - width - 1)

        for r in range(row, row + height):
            for c in range(col, col + width):
               self._map[r][c] = SPACE_SYMBOL
