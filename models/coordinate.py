class Coordinate:
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def __str__(self):
        return f"({self.row}, {self.column})"

    # properties

    @property
    def row(self):
        return self._row
    r = row

    @property
    def column(self):
        return self._column
    c = column
