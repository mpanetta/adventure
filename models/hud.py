from models.display import ENTER_PRESSED
from models.display import RESIZE

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

    def set_dungeon(self, dungeon):
        self._dungeon = dungeon
        self._update_dungeon()
        self._display.refresh()
        self._update_cursor()

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
            self._keyboard_handler(self._command_buffer)
        else:
            pass

        self._update_header()
        self._update_dungeon()
        self._display.refresh()
        self._update_cursor()

    def _clear_command_buffer(self):
        self._command_buffer = ""
        self._update_command_buffer()

    def _create_background_window(self):
        background = self._display.create_window(2, 2, 9, 52, border=True)

    def _create_dungeon_pad(self):
        self._dungeon_pad = self._display.create_pad(3, 3, 100, 100, 7, 50)

    def _create_header(self):
        self._header_window = self._display.create_window(0, 0, 2, self._display.columns)

    def _create_command_window(self):
        self._command_window = self._display.create_window(11, 0, 1, self._display.columns)

    def _header_message(self):
        return f"screen: {self._display.rows}, {self._display.columns} last key: {self._last_key}"
    
    def _update_header(self):
        self._header_window.clear()
        self._display.show_text(0, 0, self._header_message(), self._header_window)

    def _update_dungeon(self):
        if(self._dungeon == None): return

        self._dungeon.draw(self._display, self._dungeon_pad)

    def _update_cursor(self):
        self._display.set_cursor(11, 0 + len(self._command_buffer))

    def _update_command_buffer(self):
        self._command_window.clear()
        self._display.show_text(0, 0, self._command_buffer, self._command_window)
