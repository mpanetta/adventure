import curses
from curses import wrapper

class _Display(object):
    _instance = None

    # internal methods

    def __new__(klass, stdscr=None):
        if(klass._instance == None):
            klass._instance = super(_Display, klass).__new__(klass)

        return klass._instance

    # public interface

    def show_text(self, col, row, text, window=None):
        if(window == None): window = self._stdscr

        window.addstr(row, col, text)

    def refresh(self):
        for window in self._windows:
            window.refresh()

        for pad_data in self._pads:
            pad = pad_data["pad"]
            md = pad_data["metadata"]
            lrc = md["s_col"] + md["view_h"] - 1
            lrr = md["s_row"] + md["view_w"] - 1
            pad.refresh(md["p_row"], md["p_col"], md["s_row"], md["s_col"], lrr, lrc)

    def end(self, stdscr=None):
        if(stdscr != None):
            self._stdscr = stdscr

        curses.cbreak()
        self._stdscr.keypad(False)
        curses.noecho()
        curses.endwin()

    def clear(self):
        self._stdscr.clear()

    def wait(self):
        self._stdscr.getch()

    def create_window(self, row, col, height, width):
        new_window = curses.newwin(height, width, row, col)    
        self._windows.append(new_window)

        return new_window

    def create_pad(self, s_col, s_row, w, h, view_w, view_h):
        pad = curses.newpad(h, w)
        metadata = {
                "s_col": s_col,
                "s_row": s_row,
                "view_w": view_w,
                "view_h": view_h,
                "p_col": 0,
                "p_row": 0
        }
        self._pads.append({ "pad": pad, "metadata": metadata })
        return pad

    def set_cursor(self, col, row):
        self._stdscr.move(col, row)
 
    def debug_message(self, text):
        window = self._create_debugging_window()
        self.show_text(0, 0, text, window) 
        window.refresh()

    @property
    def columns(self):
        return curses.COLS

    @property
    def rows(self):
        return curses.LINES

    # private methods

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
