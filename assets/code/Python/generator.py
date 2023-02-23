import os
import json
import hashlib
import random


def gen(crooms: dict, roomdata: dict, oldpending: list):
    rnum = len(crooms)
    pending = []
    for nroom in oldpending:
        if nroom == 'STAR':
            nroom = random.choice(roomdata['rrooms'])
        num = len(crooms)
        roomdata['rooms'][nroom].setdefault('choices', [])
        crooms.setdefault(num, {})
        crooms[num].setdefault('choices', {})
        crooms[num]['text'] = roomdata['rooms'][nroom]['text']
        crooms[num].setdefault('choices', {})
        print('made ' + nroom + '(' + str(num) + ')')
        for i, choice in enumerate(roomdata['rooms'][nroom]['choices']):
            if nroom in roomdata['rrooms']:
                crooms[num]['choices'][choice] = random.randint(1, rnum)
            else:
                ranroom = random.choice(roomdata['rooms'][nroom]['proutes'][choice])
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
    for i, room in enumerate(selectedrooms):
        selectedrooms[i] = 'STAR'
    gen(rooms, data, selectedrooms)
    with open(os.path.abspath(os.getcwd()) + '/Data/crts/' + hashlib.sha256(str(rooms).encode()).hexdigest()[:10] +
              '.json', 'w') as f:
        f.write(json.dumps(rooms))
    return rooms
