import curses


def init_ui():
    """returns a new ncurses window"""
    new_screen = curses.initscr()
    curses.curs_set(False)

    return new_screen


def close_ui():
    """closes an ncurses window"""

    curses.curs_set(True)
    curses.endwin()
