""" A siple Curses-enabled Python application for managing contact information """

from time import sleep
import math
import curses


def init_ui():
    """returns a new ncurses window"""
    new_screen = curses.initscr()
    curses.curs_set(False)

    return new_screen


def display_greeter(screen) -> None:
    """displays a greeter, than closes it"""

    greeting = ["Prokop's simple addressbook app", "Manage your contacts with the help of Python and nCurses", "Made by Prokop6 <mr.prokop.6+dev@gmail.com>, Feb-Mar 2023"
                ]

    width = 0

    for val in greeting:
        if len(val) > width:
            width = len(val)

    width += 10
    height = len(greeting) * 2 + 1

    g_window = curses.newwin(height, width, math.floor(
        (curses.LINES-height)/2), math.floor((curses.COLS-width)/2))

    for i, val in enumerate(greeting):
        g_window.addstr(i*2+1, math.floor((width - len(val))/2), val)

    g_window.border()

    g_window.refresh()

    sleep(3)

    del g_window
    screen.refresh()


def close_ui():
    """closes an ncurses window"""

    curses.curs_set(True)
    curses.endwin()


def main():
    """Serves an curses-anabled app for displaying and managing an addressbook"""
    screen = init_ui()

    display_greeter(screen)
    sleep(2)

    close_ui()


if __name__ == "__main__":
    main()
