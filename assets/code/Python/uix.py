from __future__ import annotations

import os
import threading
import diypy
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
        print(tcolor + handle(btext + '\n\n', current, len(options), True))
    for option in options:
        hl = ''
        if options[current[0]] == option:
            hl = '\033[47m'
        print(hl + tcolor + handle('<center>' + option + '<\\center>', current, len(options), False) + '\033[0m')


def wfkey(val: list | None = None, keyup: str | None = None, keydown: str | None = None, btext: str | None = None,
          options: list | None = None, tcolor: str | None = None, index: int = 0, maxlen: int | None = None):
    global enterval
    mpt = threading.Thread(target=diypy.hidech)
    mpt.start()
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
            mpt.join()
            break


def handle(text: str, values: list, cint: int, ar: bool):
    tsize = os.get_terminal_size()
    y = tsize[0]
    x = tsize[1]
    if '${INDEX1}' in text:
        text = text.replace('${INDEX1}', str(values[1]))
    if '<center>' in text and '<\\center>' in text:
        oart = ''
        art = ''
        for idx in range(text.index('<center>') + 8, text.index('<\\center>')):
            oart = oart + text[idx]
        alist = oart.splitlines(False)
        alsize = 0
        for line in alist:
            alsize = len(line) if len(line) > alsize else alsize
        y = alsize + 2 if y < alsize + 2 else y
        nspace = int((tsize[0] - alsize) / 2) if y > alsize + 2 else 1
        for line in alist:
            line = ' ' * nspace + line
            line = line + ' ' * (y - len(line))
            art = art + line + '\n'
        art = art.removesuffix('\n')
        text = text.replace('<center>' + oart + '<\\center>', art)
    x = int(len(text) / y) + cint + 1 + len(text.splitlines()) if x < len(text) / y + cint + 1 + len(text.splitlines())\
        else x
    if ar:
        text = '\033[8;' + str(x) + ';' + str(y) + 't' + text
    return text


def reset_enter(dummy: None = None):
    global enterval
    enterval = True


keyboard.on_release_key('enter', reset_enter)
