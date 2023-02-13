from __future__ import annotations

import os
import threading
import keyboard
from time import sleep


def start_menu():
    kex('', ['play', 'options', 'exit'], 0, '\033[31m')


def kex(btext: str | None, options: list, current: int, tcolor: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    if btext:
        print(btext + '\n\n')
    for option in options:
        hl = ''
        if options[current] == option:
            hl = '\033[47m'
        print(hl + option + '\033[0m' + tcolor)
    nc = [current]
    dummy = threading.Thread(target=wfkey, args=[nc, 'up', 'down'])
    sleep(0.1)
    dummy.start()
    dummy.join()
    if nc[0] < 0:
        current = len(options) - 1
    elif nc[0] >= len(options):
        current = 0
    else:
        current = nc[0]
    kex(btext, options, current, tcolor)


def wfkey(val, key1, key2):
    while True:
        if keyboard.is_pressed(key1):
            val[0] -= 1
            break
        elif keyboard.is_pressed(key2):
            val[0] += 1
            break


print('This project requires your terminal to support a few things and follow a few standards, in order to check if '
      'your terminal has this standards, press "t" while in this menu or go to "options/teststd" in the main menu.\n'
      'I recommend you to NOT resize your window and let the game handle resizing.\n\npress "Enter" to continue')
while True:
    if keyboard.is_pressed('Enter'):
        start_menu()
        break
