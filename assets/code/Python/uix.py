from __future__ import annotations

import os
import keyboard
from time import sleep
enterval = True


def kex(btext: str | None, options: list, current: int, tcolor: str, up: str | None = None, down: str | None = None,
        index: int = 0, dnum: int | None = None, maxlen: int | None = None, nc: list | None = None):
    dnum = dnum or current
    if not nc:
        nc = [current]
        nc.insert(index, dnum)
    reprint(btext, options, nc, tcolor)
    sleep(0.1)
    wfkey(nc, up, down, btext, options, tcolor, index, maxlen)
    return nc[index]


def reprint(btext: str | None, options: list, current: list, tcolor: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    if btext:
        print(tcolor + replace(btext, current) + '\n\n')
    for option in options:
        hl = ''
        if options[current[0]] == option:
            hl = '\033[47m'
        print(hl + replace(option, current) + '\033[0m' + tcolor)


def wfkey(val: list | None = None, keyup: str | None = None, keydown: str | None = None, btext: str | None = None,
          options: list | None = None, tcolor: str | None = None, index: int = 0, maxlen: int | None = None):
    global enterval
    if options:
        maxlen = maxlen or len(options) - 1
    while True:
        if keyup and keyboard.is_pressed(keyup):
            val[index] -= 1
            if val[index] < 0:
                val[index] = maxlen
            reprint(btext, options, val, tcolor)
            sleep(0.1)
        elif keydown and keyboard.is_pressed(keydown):
            val[index] += 1
            if val[index] > maxlen:
                val[index] = 0
            reprint(btext, options, val, tcolor)
            sleep(0.1)
        elif keyboard.is_pressed('enter') and enterval:
            enterval = False
            break


def replace(text: str, values: list):
    if '${1}' in text:
        text = text.replace('${1}', str(values[1]))
    return text


def reset_enter(dummy: None = None):
    global enterval
    enterval = True


keyboard.on_release_key('enter', reset_enter)
