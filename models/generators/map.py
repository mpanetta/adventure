from models.generators.empty import Empty

SYMBOL_EMPTY = " "
SYMBOL_SOLID = "#"

class Map:
    def __init__(self, num_rows, num_columns):
        self._map_data = Empty(SYMBOL_SOLID).generate(num_rows, num_columns)

    # properties

    @property
    def height(self):
        return len(self._map_data)

    @property
    def width(self):
        return len(self._map_data[0])

    @property
    def map_data(self):
        return self._map_data

    # public methods

    def draw(self):
        for row in self._map_data:
            for column in row:
                print(column, end="")
            print("\r")

    def carve(self, row, column):
        self._map_data[row][column] = SYMBOL_EMPTY

    def get_neighbors(self, row, col, include_edges=False):
        if(include_edges == False):
            self._get_neighbors_excluding_edges(row, col)
        else:
            self._get_neighbors_including_edges(row, col)

    # private methods

    def _get_neighbors_excluding_edges(self, row, col):
        pass

    def _get_neighbors_including_edges(self, row, col):
        pass

