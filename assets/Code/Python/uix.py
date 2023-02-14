from __future__ import annotations

import os
import keyboard
from time import sleep


def kex(btext: str | None, options: list, current: int, tcolor: str, up: str | None = None, down: str | None = None):
    reprint(btext, options, current, tcolor)
    sleep(0.1)
    nc = [current]
    wfkey(nc, up, down, btext, options, tcolor)
    return nc[0]


def reprint(btext: str | None, options: list, current: int, tcolor: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    if btext:
        print(btext + '\n\n')
    for option in options:
        hl = ''
        if options[current] == option:
            hl = '\033[47m'
        print(hl + option + '\033[0m' + tcolor)


def wfkey(val: list | None = None, keyup: str | None = None, keydown: str | None = None, btext: str | None = None,
          options: list | None = None, tcolor: str | None = None):
    while True:
        if keyup and keyboard.is_pressed(keyup):
            val[0] -= 1
            if val[0] < 0:
                val[0] = len(options) - 1
            reprint(btext, options, val[0], tcolor)
            sleep(0.1)
        elif keydown and keyboard.is_pressed(keydown):
            val[0] += 1
            if val[0] >= len(options):
                val[0] = 0
            reprint(btext, options, val[0], tcolor)
            sleep(0.1)
        elif keyboard.is_pressed('enter'):
            break
