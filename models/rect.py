from models.coordinate import Coordinate

class Rect:
    def __init__(self, top_left, height, width):
        self._height = height
        self._width = width
        self._top_left = top_left
        self._bottom_right = Coordinate(top_left.row + height, top_left.column + width)

    def __str__(self):
        return f"{self.top_left}:{self.bottom_right} - width: {self.width}, height: {self.height}"

    # properties

    @property
    def top_left(self):
        return self._top_left
    tl = top_left

    @property
    def bottom_right(self):
        return self._bottom_right
    br = bottom_right

    @property
    def height(self):
        return self._height
    h = height

    @property
    def width(self):
        return self._width
    w = width

    # public methods

    def center(self):
        center_row = (self.top_left.row + self.bottom_right.row) // 2
        center_column = (self.top_left.column + self.bottom_right.column) // 2

        return Coordinate(center_row, center_column)

    def intersect(self, rect):
        return (self.top_left.row <= rect.bottom_right.row and self.bottom_right.row >= rect.top_left.row and
                self.top_left.column <= rect.bottom_right.column and self.bottom_right.column >= rect.top_left.column)
