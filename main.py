#! /usr/bin/env python3

""" A siple Curses-enabled Python application for managing contact information """

from view import *


def main():
    """Serves an curses-anabled app for displaying and managing an addressbook"""
    screen = init_ui()

    display_greeter(screen)

    draw_main_window(screen)

    close_ui()


if __name__ == "__main__":
    main()
