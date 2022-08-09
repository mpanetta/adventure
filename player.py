class Player:
    def __init__(self, column, row, symbol):
        self._column = column
        self._row = row
        self._symbol = symbol

    @property
    def column(self):
        return self._column

    @property
    def row(self):
        return self._row

    @property
    def symbol(self):
        return self._symbol
