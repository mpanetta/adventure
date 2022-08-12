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

class DungeonRenderer:
    def __init__(self, display, window=None, width=10, height=10):
        self._display = display
        self._window = window
    
    # properties

    @property
    def start_row(self):
        return self._row

    @property
    def start_column(self):
        return self._col
    
    @property
    def end_row(self):
        return self.start_row + self._height

    @property
    def end_column(self):
        return self.start_column + self._width 
    
    # public interface

    def set_dungeon(self, dungeon):
        self._dungeon = dungeon

    def set_view_size(self, height, width):
        self._height = height
        self._width = width

    def pan_to(self, row, col):
        self._row = max(min(row, self._dungeon.num_rows - (self._height - 1)), 0)
        self._col = max(min(col, self._dungeon.num_columns - (self._width - 1)), 0)

    def draw(self):
        view_window = self._dungeon.get_view_window(self.start_row, self.start_column, self.end_row, self.end_column)
        self._display.debug_message(f"{len(view_window)}, {len(view_window[0])} -- {self._dungeon.num_rows}, {self._dungeon.num_columns}")
        for row in range(0, len(view_window)):
            for col in range(0, len(view_window[0])):
                symbol = chr(GLYPHS[view_window[row][col]])
                self._display.show_text(col, row, symbol, window = self._window)
