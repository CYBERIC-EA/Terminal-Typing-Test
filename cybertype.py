import curses
from curses import wrapper
import time


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome to cybertype')
    stdscr.addstr('\nFeel free to test your typing skills')
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, character in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(3)
        if character != correct_char:
            color = curses.color_pair(4)

        stdscr.addstr(0, i, character, color)


def words_per_minutes_test(stdscr):
    text_to_display = 'insert text to be typed here'
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, text_to_display, current_text, wpm)
        stdscr.refresh()

        if (''.join(current_text) == text_to_display):
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        if key in ('KEY_BACKSPACE', '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(text_to_display):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)
    words_per_minutes_test(stdscr)

    stdscr.addstr(
        2, 0, 'You completed the typing challenge. Press any key to continue...')

    stdscr.getkey()


wrapper(main)
