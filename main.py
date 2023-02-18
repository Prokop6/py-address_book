""" A siple Curses-enabled Python application for managing contact information """

import curses
from time import sleep


def main():

    new_screen = curses.initscr()

    new_screen.addstr(2, 2, "Hello, World!")

    new_screen.refresh()

    sleep(3)

    curses.endwin()


if __name__ == "__main__":
    main()
