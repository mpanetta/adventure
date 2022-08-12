from models.display import ENTER_PRESSED
from models.display import RESIZE
from models.dungeon_renderer import DungeonRenderer
from models.logger import Logger

_DUNGEON_WINDOW_HEIGHT = 7
_DUNGEON_WINDOW_WIDTH = 50
_DUNGEON_WINDOW_ROW = 3
_DUNGEON_WINDOW_COL = 3

_COMMAND_COL = 0
_COMMAND_HEIGHT = 1

class Hud:
    def __init__(self, display, keyboard_handler):
        self._display = display
        self._keyboard_handler = keyboard_handler
        self._command_buffer = ""
        self._last_key = 1
        self._dungeon = None
        
        self._create_background_window()
        self._create_dungeon_pad()
        self._create_header()
        self._update_header()
        self._create_command_window()
        self._display.refresh()
        self._update_cursor()

        self._dungeon_renderer = DungeonRenderer(self._display, self._dungeon_pad)

    # properties

    # public interface

    def set_dungeon(self, dungeon):
        self._dungeon = dungeon
        self._dungeon_renderer.set_dungeon(dungeon)
        self._dungeon_renderer.set_view_size(_DUNGEON_WINDOW_HEIGHT, _DUNGEON_WINDOW_WIDTH)
        self._dungeon_renderer.pan_to(0, 0)
        self._update_dungeon()
        self._display.refresh()
        self._update_cursor()

    def scroll_dungeon(self, col, row):
        pass

    def wait(self):
        self._display.input()

    def start_keyboard(self):
        self._display.start_keyboard(self.keyboard_handler)

    def keyboard_handler(self, character):
        self._last_key = character

        if(character == ENTER_PRESSED):
            self._keyboard_handler(self._command_buffer)
            self._clear_command_buffer()
        elif(character == RESIZE):
            self._display.debug_message("resizing")
        elif(character != None):
            self._command_buffer += character
            self._update_command_buffer()
            if(self._keyboard_handler(self._command_buffer) == True):
                self._clear_command_buffer()
        else:
            pass

        self._update_header()
        self._update_dungeon()
        self._display.refresh()
        self._update_cursor()

    def flush_command(self):
        self._clear_command_buffer()

    # private methods

    def _clear_command_buffer(self):
        self._command_buffer = ""
        self._update_command_buffer()

    def _create_background_window(self):
        br, bc = _DUNGEON_WINDOW_ROW - 1, _DUNGEON_WINDOW_COL - 1
        background = self._display.create_window(br, bc, _DUNGEON_WINDOW_HEIGHT + 2, _DUNGEON_WINDOW_WIDTH + 2, border=True)

    def _create_dungeon_pad(self):
        self._dungeon_pad = self._display.create_pad(_DUNGEON_WINDOW_ROW, _DUNGEON_WINDOW_COL, 100, 100, _DUNGEON_WINDOW_HEIGHT, _DUNGEON_WINDOW_WIDTH)

    def _create_header(self):
        self._header_window = self._display.create_window(0, 0, 2, self._display.columns)

    def _create_command_window(self):
        hr = _DUNGEON_WINDOW_ROW + _DUNGEON_WINDOW_HEIGHT + 1
        self._command_window = self._display.create_window(hr, _COMMAND_COL, _COMMAND_HEIGHT, self._display.columns)

    def _header_message(self):
        return f"screen: {self._display.rows}, {self._display.columns} last key: {self._last_key}"
    
    def _update_header(self):
        self._header_window.clear()
        self._display.show_text(0, 0, self._header_message(), self._header_window)

    def _update_dungeon(self):
        if(self._dungeon == None): return
        self._dungeon_renderer.draw()

    def _update_cursor(self):
        cursor_col = _DUNGEON_WINDOW_ROW + _DUNGEON_WINDOW_HEIGHT + 1
        self._display.set_cursor(cursor_col,  _COMMAND_COL + len(self._command_buffer))

    def _update_command_buffer(self):
        self._command_window.clear()
        self._display.show_text(0, 0, self._command_buffer, self._command_window)
