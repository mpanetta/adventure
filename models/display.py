import curses
from curses import wrapper

ENTER_PRESSED = -1
RESIZE = -2

class _Display(object):
    _instance = None

    # internal methods

    def __new__(klass, stdscr=None):
        if(klass._instance == None):
            klass._instance = super(_Display, klass).__new__(klass)

        return klass._instance

    # public interface

    @property
    def columns(self):
        return curses.COLS

    @property
    def rows(self):
        return curses.LINES

    def show_text(self, col, row, text, window=None):
        if(window == None): window = self._stdscr

        window.addstr(row, col, text)

    def debug_message(self, text):
        window = self._create_debugging_window()
        self.show_text(0, 0, text, window) 
        window.refresh()

    def refresh(self):
        for window in self._windows:
            window.refresh()

        for pad_data in self._pads:
            pad = pad_data["pad"]
            md = pad_data["metadata"]
            lrc = md["s_col"] + md["view_w"] - 1
            lrr = md["s_row"] + md["view_h"] - 1
            pad.refresh(md["p_row"], md["p_col"], md["s_row"], md["s_col"], lrr, lrc)

    def end(self, stdscr=None):
        if(stdscr != None): self._stdscr = stdscr

        curses.cbreak()
        self._stdscr.keypad(False)
        curses.noecho()
        curses.endwin()

    def clear(self):
        self._stdscr.clear()

    def create_window(self, row, col, height, width):
        new_window = curses.newwin(height, width, row, col)    
        self._windows.append(new_window)

        return new_window

    def create_pad(self, s_row, s_col, h, w, view_h, view_w):
        pad = curses.newpad(h, w)
        metadata = {
                "s_row": s_row,
                "s_col": s_col,
                "view_h": view_h,
                "view_w": view_w,
                "p_row": 0,
                "p_col": 0
        }

        self._pads.append({ "pad": pad, "metadata": metadata })
        return pad

    def set_cursor(self, col, row):
        self._stdscr.move(col, row)

    def input(self):
        return self._stdscr.getch()

    def register_keyboard_handler(self, handler):
        self._keyboard_handlers.append(handler)

    def stop_keyboard(self):
        self._break = True

    def start_keyboard(self, handler=None):
        if(handler != None): self.register_keyboard_handler(handler)
        self._break = False 

        while(self._break != True):
            c = self.input()
            character = self._determine_character(c)

            for h in self._keyboard_handlers:
                h(character)

    # private methods

    def _determine_character(self, c):
        if(c == curses.KEY_ENTER or c == 10 or c == 13):
            return ENTER_PRESSED
        elif(c == -1):
            return RESIZE
        elif(c >= 0 and c <= 255):
            return chr(c)
        else:
            return None

    def _start(self, stdscr=None):
        if(stdscr != None):
            self._stdscr = stdscr
        else:
            self._stdscr = curses.initscr()
            _stdscr.keypad(True)

            curses.noecho()
            curses.cbreak()

        self._windows = list([stdscr])
        self._pads = list([])
        self._debugging_window = None
        self._keyboard_handlers = list([])
        self.clear()

    def _create_debugging_window(self):
        if(self._debugging_window != None): return self._debugging_window

        height, width = 4, self.columns - 1
        row, col = self.rows - height, 0
        self._debugging_window = self.create_window(row, col, height, width)

        return self._debugging_window

def display_decorator(func):
    def internal_expression(stdscr, *args, **kwargs):
        display = kwargs.get("display")
        display._start(stdscr)

        func(*args, **kwargs)

    def internal_wrapper(*args, **kwargs):
        display = kwargs.get("display")
        wrapper(lambda stdscr : internal_expression(stdscr, *args, **kwargs))

    return internal_wrapper

Display = _Display()
