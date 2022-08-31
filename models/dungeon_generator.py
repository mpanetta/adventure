from models.node import Node
from models.room import Room
from models.rect import Rect
from models.coordinate import Coordinate

import random
import string
import time

ROCK_SYMBOL = "#"
SPACE_SYMBOL = " "
MIN_WIDTH = 4
MAX_WIDTH = 16
MIN_HEIGHT = 2
MAX_HEIGHT = 8
SMOOTHING = 1
FILLING = 3

class DungeonGenerator:
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._root_node = Node(0, 0, height, width)
        self._map = self._generate_solid_dungeon(height, width)

        self._root_node.split()
        self._build_rooms()
        self._connect_rooms(self._root_node)
        self.draw()
        self._cleanup()
        print("\n\nAFTER:")
        self.draw()

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
        node.room = Room(Rect(Coordinate(row, col), height, width), node)

        for r in range(row, row + height):
            for c in range(col, col + width):
               self._map[r][c] = SPACE_SYMBOL

    def _connect_rooms(self, node):
        if(node.left != None and node.right != None):
            self._connect_room(node.left.room, node.right.room)

        if(node.left != None): self._connect_rooms(node.left)
        if(node.right != None): self._connect_rooms(node.right)

    def _connect_room(self, room1, room2):
        if(room1 == None or room2 == None): return

        start = room2.center
        goal = room1.center

        self._map[start.row][start.column] = 1
        self._map[goal.row][goal.column] = 2

        # while not((room1.top_left.row < room2.center.row < room1.bottom_right.row) or
        #       not (room1.top_left.column <= room2.center.column <= room2.bottom_right.column)):

        while not(start.column == goal.column and start.row == goal.row):
            north, south, east, west, weight = 1.0, 1.0, 1.0, 1.0, 1.0

            if(start.column < goal.column):
                east += weight
            if(start.column > goal.column):
                west += weight
            if(start.row < goal.row):
                south += weight
            if(start.row > goal.row):
                north += weight

            total = north + south + east + west
            north /= total
            south /= total
            east /= total
            west /= total

            choice = random.random()
            if(0 <= choice <= north):
                dx = 0
                dy = -1
            elif(north <= choice < (north + south)):
                dx = 0
                dy = 1
            elif((north + south) <= choice  < (north + south + east)):
                dx = 1
                dy = 0
            else:
                dx = -1
                dy = 0

            if((0 < start.row + dy < self._height -1) and (0 < start.column + dx < self._width - 1)):
                start = Coordinate(start.row + dy, start.column + dx)

                if(self._map[start.row][start.column] == ROCK_SYMBOL):
                    self._map[start.row][start.column] = SPACE_SYMBOL

    def _cleanup(self):
        for i in range(3):
            for c in range(1, self._width - 1):
                for r in range(1, self._height - 1):
                    if((self._map[r][c] == ROCK_SYMBOL) and (self._get_walls_score(r, c) <= SMOOTHING)):
                        self._map[r][c] = SPACE_SYMBOL
                    if((self._map[r][c] == SPACE_SYMBOL) and (self._get_walls_score(r, c) >= FILLING)):
                        self._map[r][c] = ROCK_SYMBOL

    def _get_walls_score(self, row, column):
        count = 0
        if(self._map[row-1][column] == ROCK_SYMBOL):
            count += 1
        if(self._map[row+1][column] == ROCK_SYMBOL):
            count += 1
        if(self._map[row][column - 1] == ROCK_SYMBOL):
            count += 1
        if(self._map[row][column + 1] == ROCK_SYMBOL):
            count += 1

        return count
