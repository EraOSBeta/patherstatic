from __future__ import annotations

import termios
import uix
import logo
from time import sleep


def start_menu():
    choice = uix.kex('', ['play', 'options', 'exit'], 0, '\033[31m', 'up', 'down')
    if choice == 0:
        play_menu()
    elif choice == 1:
        options_menu()
    elif choice == 2:
        end()


def play_menu():
    """tba"""


def options_menu():
    choice = uix.kex('A list of options and settings', ['teststd', 'display logo', 'return'], 0, '\033[31m', 'up',
                     'down')
    if choice == 0:
        print('\033[32m this text should be green\n\n\033[47m\033[30mand this\nshould b\ne a squa\nre      \033[0m')
        sleep(0.1)
        uix.wfkey()
        options_menu()
    elif choice == 1:
        logo.dis()
        options_menu()
    elif choice == 2:
        start_menu()


def end():
    termios.tcflush(0, termios.TCIFLUSH)
    quit()


print('This project requires your terminal to support a few things and follow a few standards, in order to check if '
      'your terminal has this standards, press "t" while in this menu or go to "options/teststd" in the main menu.\n'
      'I recommend you to NOT resize your window and let the game handle resizing.\n\npress "Enter" to continue')
uix.wfkey()
start_menu()
termios.tcflush(0, termios.TCIFLUSH)
