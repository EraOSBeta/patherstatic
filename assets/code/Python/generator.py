import os
import json
import hashlib
import random


def gen(crooms: dict, roomdata: dict, oldpending: list):
    pending = []
    for nroom in oldpending:
        num = len(crooms)
        roomdata[nroom].setdefault('choices', [])
        crooms.setdefault(num, {})
        crooms[num]['text'] = roomdata[nroom]['text']
        crooms[num].setdefault('choices', {})
        print('made ' + nroom + '(' + str(num) + ')')
        for i, choice in enumerate(roomdata[nroom]['choices']):
            ranroom = random.choice(roomdata[nroom]['proutes'][choice])
            crooms[num]['choices'][choice] = choice_counter(crooms) + 1
            pending.append(ranroom)
    return [len(crooms), pending]


def choice_counter(tocount: dict):
    counter = 0
    for r in tocount:
        counter += len(tocount[r]['choices'])
    return counter


def new(roomint: int):
    with open(os.path.abspath(os.getcwd()) + '/Data/generic/rooms.json') as f:
        data = json.loads(f.read())
    selectedrooms = [random.choice(data['srooms'])]
    rooms = {}
    numn = 0
    while numn <= roomint:
        fback = gen(rooms, data, selectedrooms)
        numn = fback[0]
        selectedrooms = fback[1]
    with open(os.path.abspath(os.getcwd()) + '/Data/crts/' + hashlib.sha256(str(rooms).encode()).hexdigest()[:10] + '.json',
              'w') as f:
        f.write(json.dumps(rooms))
    return rooms
