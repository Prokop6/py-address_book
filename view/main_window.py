"""creates main window of the application"""

import curses
from math import floor

from .ui import close_ui


def draw_main_window(screen) -> None:

    try:
        SCREEN_WIDTH = curses.COLS
        SCREEN_HEIGHT = curses.LINES

        PANEL_WIDTH = floor(SCREEN_WIDTH / 3)
        PANEL_HEIGHT = floor(SCREEN_HEIGHT / 3)

        list_window = curses.newwin(
            SCREEN_HEIGHT - PANEL_HEIGHT, PANEL_WIDTH, 0, 0)

        options_window = curses.newwin(
            PANEL_HEIGHT, PANEL_WIDTH, SCREEN_HEIGHT-PANEL_HEIGHT, 0)

        result_window = curses.newwin(
            SCREEN_HEIGHT, SCREEN_WIDTH-PANEL_WIDTH, 0, PANEL_WIDTH)

        list_window.border()
        options_window.border()
        result_window.border()

        list_window.refresh()
        options_window.refresh()
        result_window.refresh()

        screen.refresh()

        active = True

        while active:
            input = screen.getkey()

            if input == "q":
                active = False
            else:
                curses.flash()

        del list_window
        del options_window
        del result_window

        screen.refresh()

    except Exception as exc:

        close_ui()
