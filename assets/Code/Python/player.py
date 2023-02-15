from __future__ import annotations

import os
import termios
import json
import uix
import generator
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
    pcrts = os.scandir(os.path.abspath(os.getcwd()) + '/Data/crts')
    crts = []
    for crt in pcrts:
        if crt.is_file() and crt.name.endswith('.json'):
            crts.append(crt.name.removesuffix('.json'))
    crts.extend(['GENERATE A NEW CARTRIDGE', 'return'])
    crt = uix.kex('Choose a cartridge', crts, 0, '\033[31m', 'up', 'down')
    if crt == len(crts) - 1:
        start_menu()
    elif crt == len(crts) - 2:
        gen_menu(20)
    else:
        with open(os.path.abspath(os.getcwd()) + '/Data/crts/' + crts[crt] + '.json') as f:
            data = json.loads(f.read())
        load_crt(data)


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


def gen_menu(dr):
    c = uix.kex('gen options: ', ['preferred room count: ${1}', 'GENERATE', 'return'], 0, '\033[31m', 'up', 'down')
    if c == 0:
        sleep(0.2)
        dr = uix.kex('gen options: ', ['preferred room count: ${1}', 'GENERATE', 'return'], 0, '\033[31m', 'left',
                     'right', 1, 20, 999999)
        gen_menu(dr)
    elif c == 1:
        generator.new(dr)
        play_menu()
    else:
        play_menu()


def load_crt(crt: dict):
    """tba"""


print('This project requires your terminal to support a few things and follow a few standards, in order to check if '
      'your terminal has this standards, go to "options/teststd" in the main menu.\nI recommend you to NOT resize '
      'your window and let the game handle resizing.\n\npress "Enter" to continue')
uix.wfkey()
start_menu()
termios.tcflush(0, termios.TCIFLUSH)
