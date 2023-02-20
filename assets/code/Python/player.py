from __future__ import annotations

import os
import termios
import json
import uix
import generator
import logo


def main_process():
    oc = start_menu
    c = start_menu
    while c:
        if callable(c):
            oc = c
            c = c()
        elif type(c) is dict:
            froom = 0
            while froom >= 0:
                froom = load_crt(c, froom)
        else:
            c = oc(c)


def start_menu():
    choice = uix.kex('', ['play', 'options', 'exit'], 0, '\033[31m', 'up', 'down')
    if choice == 0:
        return play_menu
    elif choice == 1:
        return options_menu
    elif choice == 2:
        return end


def play_menu():
    pcrts = os.scandir(os.path.abspath(os.getcwd()) + '/Data/crts')
    crts = []
    for crt in pcrts:
        if crt.is_file() and crt.name.endswith('.json'):
            crts.append(crt.name.removesuffix('.json'))
    crts.extend(['GENERATE A NEW CARTRIDGE', 'return'])
    crt = uix.kex('Choose a cartridge', crts, 0, '\033[31m', 'up', 'down')
    if crt == len(crts) - 1:
        return start_menu
    elif crt == len(crts) - 2:
        return gen_menu
    else:
        with open(os.path.abspath(os.getcwd()) + '/Data/crts/' + crts[crt] + '.json') as f:
            return json.loads(f.read())


def options_menu():
    choice = uix.kex('A list of options and settings', ['teststd', 'display logo', 'return'], 0, '\033[31m', 'up',
                     'down')
    if choice == 0:
        print('\033[32m this text should be green\n\n\033[47m\033[30mand this\nshould b\ne a squa\nre      \033[0m')
        uix.wfkey()
        return options_menu
    elif choice == 1:
        logo.dis()
        return options_menu
    elif choice == 2:
        return start_menu


def end():
    termios.tcflush(0, termios.TCIFLUSH)
    quit()


def gen_menu(dr: int = 20):
    c = uix.kex(btext='gen options: ', options=['preferred room count: ${1}', 'GENERATE', 'return'], current=0,
                tcolor='\033[31m', up='up', down='down', nc=[0, dr])
    if c == 0:
        dr = uix.kex('gen options: ', ['preferred room count: ${1}', 'GENERATE', 'return'], 0, '\033[31m', 'left',
                     'right', 1, 20, 999999, [0, dr])
        return dr
    elif c == 1:
        generator.new(dr)
        return play_menu
    else:
        return play_menu


def load_crt(crt: dict, room: str | int):
    room = str(room)
    choices = []
    for choice in crt[room]['choices']:
        choices.append(choice)
    choice = uix.kex(crt[room]['text'], choices, 0, '', 'up', 'down')
    for i, v in enumerate(crt[room]['choices']):
        if i == choice:
            return crt[room]['choices'][v]


print('This project requires your terminal to support a few things and follow a few standards, in order to check if '
      'your terminal has this standards, go to "options/teststd" in the main menu.\nI recommend you to NOT resize '
      'your window and let the game handle resizing.\n\npress "Enter" to continue')
uix.wfkey()
main_process()
termios.tcflush(0, termios.TCIFLUSH)
