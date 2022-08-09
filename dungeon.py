# Dungeon unicode characters

GLYPHS = {
    "TL": 9484,
    "BL": 9492,
    "TR": 9488,
    "BR": 9496,
    "HH": 9472,
    "VV": 9474,
    "EE": 32,
    "PL": 9791
}

class Dungeon:
    def __init__(self, filename):
        self._load_dungeon(filename)
        self._set_dimensions()
        self._objects = []

    def draw(self, display, window=None):
        for column in range(0, self._num_columns):
            for row in range(0, self._num_rows):
                glyph = GLYPHS[self._map[column][row]]
                obj = self._get_object(column, row)
                character = (chr(glyph) if obj == None else obj.symbol)

                display.show_text(column, row, character, window=window)

    def add_object(self, obj):
        if(self.is_passable(obj.column, obj.row) == False): return False
        self._objects.append(obj)
        return True

    def is_passable(self, column, row):
        if(self._get_object(column, row) != None): return False
        if(self._map[column][row] != "EE"): return False
        return True

    # private methods

    def _load_dungeon(self, filename):
        self._map = []

        with open(filename) as file:
            lines = file.readlines()
            for line in lines:
                row = []
                for character in line.split(","):
                    row.append(character.strip())
                self._map.append(row)

    def _set_dimensions(self):
        self._num_columns = len(self._map)
        self._num_rows = len(self._map[0])

    def _get_object(self, column, row):
       for obj in self._objects:
           if(obj.column == column and obj.row == row):
               return obj
