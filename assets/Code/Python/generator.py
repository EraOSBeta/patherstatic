import os
import json
import random


def gen(crooms: dict, roomdata: dict, nroom: str, maxnum: int, pending: list, process: int):
    num = len(crooms)
    crooms.setdefault(num, {})
    crooms[num]['text'] = roomdata[nroom]['text']
    roomdata[nroom].setdefault('choices', [])
    for i, choice in enumerate(roomdata[nroom]['choices']):
        if num < maxnum:
            crooms[num].setdefault('choices', {})
            ranroom = random.choice(roomdata[nroom]['proutes'][choice])
            crooms[num]['choices'][choice] = len(crooms) + i
            pending = gen(crooms, roomdata, ranroom, maxnum, pending, process + 1)
    if process <= 0:
        for i, v in enumerate(pending):
            pending.pop(i)
            gen(crooms, roomdata, v, maxnum, pending, process)
    return pending


name = input('What\'s gonna be the name of your cartridge? (str) ') or 'invalid name'
try:
    roomint = int(input('how many rooms would you like to be in your cartridge? (int) ')) - 1
except ValueError:
    roomint = 20
print('opening rooms.json...')
with open(os.path.abspath(os.getcwd()) + '/../../Data/rooms.json') as f:
    data = json.loads(f.read())

print('will generate rooms now...')
starterroom = random.choice(data['srooms'])
rooms = {}
gen(rooms, data, starterroom, roomint, [], 0)

with open(os.path.abspath(os.getcwd()) + '/' + name + '.json', 'w') as f:
    f.write(json.dumps(rooms))
print('Done!')
