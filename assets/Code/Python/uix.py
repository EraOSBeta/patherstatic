from __future__ import annotations

import os
import keyboard
from time import sleep


def kex(btext: str | None, options: list, current: int, tcolor: str, up: str | None = None, down: str | None = None,
        index: int = 0):
    reprint(btext, options, [current], tcolor)
    sleep(0.1)
    nc = [current]
    wfkey(nc, up, down, btext, options, tcolor, index)
    return nc[0]


def reprint(btext: str | None, options: list, current: list, tcolor: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    if btext:
        print(tcolor + btext + '\n\n')
    for option in options:
        hl = ''
        if options[current[0]] == option:
            hl = '\033[47m'
        print(hl + option + '\033[0m' + tcolor)


def wfkey(val: list | None = None, keyup: str | None = None, keydown: str | None = None, btext: str | None = None,
          options: list | None = None, tcolor: str | None = None, index: int = 0):
    while True:
        if keyup and keyboard.is_pressed(keyup):
            val[index] -= 1
            if val[index] < 0:
                val[index] = len(options) - 1
            reprint(btext, options, val, tcolor)
            sleep(0.1)
        elif keydown and keyboard.is_pressed(keydown):
            val[index] += 1
            if val[index] >= len(options):
                val[index] = 0
            reprint(btext, options, val, tcolor)
            sleep(0.1)
        elif keyboard.is_pressed('enter'):
            break
