""" A siple Curses-enabled Python application for managing contact information """

from ui import *
from time import sleep




def main():
    """Serves an curses-anabled app for displaying and managing an addressbook"""
    screen = init_ui()

    display_greeter(screen)
    sleep(2)

    close_ui()


if __name__ == "__main__":
    main()
