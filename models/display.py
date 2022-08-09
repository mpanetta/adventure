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

        window.addstr(col, row, text)

    def refresh(self):
        for window in self._windows:
            window.refresh()

    def end(self, stdscr=None):
        if(stdscr != None):
            self._stdscr = stdscr

        curses.cbreak()
        self._stdscr.keypad(False)
        curses.noecho()
        curses.endwin()

    def clear(self):
        self._stdscr.clear()

    def create_window(self, col, row, width, height):
        new_window = curses.newwin(height, width, row, col)    
        self._windows.append(new_window)

        return new_window
    
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
        self._debugging_window = None
        self.clear()

    def _create_debugging_window(self):
        if(self._debugging_window != None): return self._debugging_window
        width, height = self.columns - 1, 4
        col, row = 0, self.rows - 1 - height
        self._debugging_window = self.create_window(col, row, width, height)

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
