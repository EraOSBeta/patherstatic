import os
import json
import random


def gen(crooms: dict, roomdata: dict, oldpending: list):
    pending = []
    for nroom in oldpending:
        num = len(crooms)
        roomdata[nroom].setdefault('choices', [])
        crooms.setdefault(num, {})
        crooms[num]['text'] = roomdata[nroom]['text']
        crooms[num].setdefault('choices', {})
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


name = input('What\'s gonna be the name of your cartridge? (str) ') or 'invalid name'
try:
    roomint = int(input('how many rooms would you like to be in your cartridge? (int) ')) - 1
except ValueError:
    roomint = 20
print('opening rooms.json...')
with open(os.path.abspath(os.getcwd()) + '/../../Data/rooms.json') as f:
    data = json.loads(f.read())

print('will generate rooms now...')
selectedrooms = [random.choice(data['srooms'])]
rooms = {}
numn = 0
while numn <= roomint:
    fback = gen(rooms, data, selectedrooms)
    numn = fback[0]
    selectedrooms = fback[1]

with open(os.path.abspath(os.getcwd()) + '/' + name + '.json', 'w') as f:
    f.write(json.dumps(rooms))
print('Done!')
