import curses


def init_ui():
    """returns a new ncurses window"""
    new_screen = curses.initscr()
    curses.curs_set(False)
    curses.noecho()

    return new_screen


def close_ui():
    """closes an ncurses window"""

    curses.echo()
    curses.curs_set(True)
    curses.endwin()
