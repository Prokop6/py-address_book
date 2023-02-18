import curses
import math
from time import sleep


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
