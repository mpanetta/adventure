class Player:
    def __init__(self, column, row, symbol):
        self._column = column
        self._row = row
        self._symbol = symbol

    @property
    def column(self):
        return self._column
    
    @column.setter
    def column(self, value):
        self._column = value

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        self._row = value

    @property
    def symbol(self):
        return self._symbol
