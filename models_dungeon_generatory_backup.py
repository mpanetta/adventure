import random

from models.logger import Logger

class Point:
    def __init__(self, row, col):
        self._row = row
        self._column = col

    def __str__(self):
        return f"({self.row}, {self.col})"

    # properties

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._column

class Subdivision:
    def __init__(self, top_left, bottom_right):
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._left = None
        self._right = None

    def __str__(self):
        return f"TL: {self.top_left} BR: {self.bottom_right} W: {self.width} H: {self.height}"

    # properties

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, division):
        self._left = division

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, division):
        self._right = division

    @property
    def is_divisible(self):
        return self.height >= 4 and self.width >= 8

    @property
    def top_left(self):
        return self._top_left

    @property
    def bottom_right(self):
        return self._bottom_right

    @property
    def width(self):
        return self._bottom_right.col - self._top_left.col

    @property
    def height(self):
        return self._bottom_right.row - self._top_left.row

    @property
    def is_terminal(self):
        return (self._left == None and self._right == None)

    @property
    def is_valid(self):
        return self.height >= 4 and self.width >= 4

    # public methods

    def terminal_nodes(self, node, nodes=[], count=1):
        Logger.log(f"Nodes: {len(nodes)}, COUNT: {count}")
        if(node.is_terminal == True):
            nodes.append(node)
            return

        if(node.left != None):
            count += 1
            self.terminal_nodes(node.left, nodes, count)
        if(node.right != None):
            count += 1
            self.terminal_nodes(node.right, nodes, count)
        return nodes

    def valid_nodes(self):
        return [node for node in self.terminal_nodes(self) if node.is_valid]

    def divide_on_column(self, column):
        rect1_tl = Point(self.top_left.row, self.top_left.row)
        rect1_br = Point(self.bottom_right.row, self.top_left.col + column - 1)

        rect2_tl = Point(self.top_left.row, self.top_left.col + column)
        rect2_br = Point(self.bottom_right.row, self.bottom_right.col)

        division1 = Subdivision(rect1_tl, rect1_br)
        division2 = Subdivision(rect2_tl, rect2_br)

        return division1, division2

    def divide_on_row(self, row):
        rect1_tl = Point(self.top_left.col, self.top_left.row)
        rect1_br = Point(self.top_left.row + row, self.bottom_right.col)

        rect2_tl = Point(self.top_left.row + row + 1, self.top_left.col)
        rect2_br = Point(self.bottom_right.row, self.bottom_right.col)

        division1 = Subdivision(rect1_tl, rect1_br)
        division2 = Subdivision(rect2_tl, rect2_br)

        return division1, division2


class DungeonGenerator:
    def __init__(self):
        self._rooms = []

    # public methods

    def generate(self, num_rows, num_cols):
        base_dungeon = self._generate_solid_dungeon(num_rows, num_cols)
        root_division = Subdivision(Point(0, 0), Point(num_rows - 1, num_cols - 1))
        self._build_subdivisions(root_division)

        self._carve_rooms(base_dungeon, root_division.valid_nodes())
        # self._mark(root_division, base_dungeon)

        return base_dungeon

    # private methods

    def _mark(self, root_division, map):
        i = 0
        for node in root_division.valid_nodes():
            Logger.log(f"INDEX: {i} ::: ROOM: {node}")
            map[node.top_left.row][node.top_left.col] = i
            map[node.bottom_right.row][node.bottom_right.col] = i
            i += 1

    def _carve_rooms(self, base_dungeon, valid_nodes):
        for node in valid_nodes:
            # Logger.log(f"NODE TO MAKE ROOM: {node}")

            height = random.randint(2, node.height - 2)
            width = random.randint(2, node.width - 2)
            row = random.randint(1, node.height - height) + node.top_left.row
            col = random.randint(1, node.width - width) + node.top_left.col

            # Logger.log(f"ROOM::: ({row}, {col}), ({row + height}, {col + width}) :: ({height}, {width})")
            self._rooms.append(f"({row}, {col}) :: ({height}, {width})")
            for r in range(row, row + height - 1):
                for c in range(col, col + width - 1):
                    base_dungeon[r][c] = " "

    def _generate_solid_dungeon(self, num_rows, num_cols):
        dungeon = []

        for row in range(0, num_rows):
            dungeon.append([])
            for col in range(0, num_cols):
                dungeon[row].append("#")

        return dungeon

    def _build_subdivisions(self, subdivision):
        div1, div2 = self._subdivide(subdivision)
        subdivision.left = div1
        subdivision.right = div2

        for div in [div1, div2]:
            if(div.is_divisible): self._build_subdivisions(div)

    def _subdivide(self, subdivision):
        Logger.log(f"W: {subdivision.width} - H: {subdivision.height}")
        if(subdivision.height >= subdivision.width):
            return self._subdivide_horizontal(subdivision)
        else:
            return self._subdivide_vertical(subdivision)

    def _subdivide_vertical(self, subd):
        quarter_width = max(2, subd.height // 4)
        column = random.randint(quarter_width, subd.width - quarter_width)

        return subd.divide_on_column(column)

    def _subdivide_horizontal(self, subd):
        quarter_height = max(2, subd.height // 4)
        row = random.randint(quarter_height, subd.height - quarter_height)

        return subd.divide_on_row(row)
