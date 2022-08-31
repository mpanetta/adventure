from models.rect import Rect
from models.coordinate import Coordinate

import random

HORIZONTAL = "horizontal"
VERTICAL = "vertical"
MIN_WIDTH = 20
MIN_HEIGHT = 10

class Node:
    _all_nodes = []

    def __init__(self, row, column, height, width):
       top_left = Coordinate(row, column)
       self._all_nodes = []
       self._rectangle = Rect(top_left, height, width)
       self._left = None
       self._right = None

    def __str__(self):
        return f"{self._rectangle}"

    @classmethod
    def from_coordinate(klass, coordinate, height, width):
        return klass(coordinate.row, coordinate.column, height, width)

    # properties

    @property
    def row(self):
        return self._rectangle.top_left.row
    r = row

    @property
    def column(self):
        return self._rectangle.top_left.column
    c = column

    @property
    def top_left(self):
        return self._rectangle.top_left
    tl = top_left

    @property
    def bottom_right(self):
        return self._rectangle.bottom_right
    br = bottom_right

    @property
    def width(self):
        return self._rectangle.width
    w = width

    @property
    def height(self):
        return self._rectangle.height
    h = height

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    @property
    def rectangle(self):
        return self._rectangle

    # public methods

    def split(self):
        if(self._split_direction() == VERTICAL):
            if(self.width - MIN_WIDTH >= MIN_WIDTH):
                self.left, self.right = self._split_vertically()
        else:
            if(self.height - MIN_HEIGHT >= MIN_HEIGHT):
                self.left, self.right = self._split_horizontally()

        if(self.left != None): self.left.split()
        if(self.right != None): self.right.split()

    def is_terminal(self):
        return (self.left == None and self.right == None)

    def terminal_nodes(self):
       nodes = []

       if(self.is_terminal()): nodes.append(self)
       if(self.left != None): nodes.extend(self.left.terminal_nodes())
       if(self.right != None): nodes.extend(self.right.terminal_nodes())

       return nodes

    # private methods

    def _split_direction(self):
        if(self.width / self.height >= 1.25):
            return VERTICAL
        elif(self.height / self.width > 1.25):
            return HORIZONTAL
        else:
            return random.choice([HORIZONTAL, VERTICAL])

    def _split_vertically(self):
        max = self.width - MIN_WIDTH
        split = random.randint(MIN_WIDTH, max)

        left_node = Node(self.row, self.column, self.height, split)
        right_node = Node(self.row, self.column + split + 1, self.height, self.width - split - 1)

        Node._all_nodes.append(left_node)
        Node._all_nodes.append(right_node)

        return left_node, right_node

    def _split_horizontally(self):
        max = self.height - MIN_HEIGHT
        split = random.randint(MIN_HEIGHT, max)

        left_node = Node(self.row, self.column, split, self.width)
        right_node = Node(self.row + split + 1, self.column, self.height - split - 1, self.width)

        Node._all_nodes.append(left_node)
        Node._all_nodes.append(right_node)

        return left_node, right_node
