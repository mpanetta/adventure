class Dungeon:
    def __init__(self, filename):
        self._load_dungeon(filename)
        self._set_dimensions()
        self._objects = []

    # properties

    @property
    def num_columns(self):
        return self._num_columns

    @property
    def num_rows(self):
        return self._num_rows

    # public methods

    def get_view_window(self, start_row, start_col, end_row, end_col):
        view_window = []
        for row in range(start_row, end_row + 1):
            if(row >= self.num_rows): continue

            view_row = []
            for col in range(start_col, end_col + 1):
                if(col >= self.num_columns): continue

                obj = self._get_object(row, col)
                character = self._map[row][col] if obj == None else obj.symbol
                view_row.append(character)
            view_window.append(view_row)

        return view_window

    def add_object(self, obj):
        if(self.is_passable(obj.row, obj.column) == False): return False
        self._objects.append(obj)
        return True

    def is_passable(self, row, column):
        if(self._get_object(column, row) != None): return False
        if(self._map[row][column] != "EE"): return False
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
        self._num_rows = len(self._map)
        self._num_columns = len(self._map[0])

    def _get_object(self, row, column):
       for obj in self._objects:
           if(obj.row == row and obj.column == column):
               return obj
