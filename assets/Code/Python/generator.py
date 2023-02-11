import os
import json
import random


def gen(crooms: dict, roomdata: dict, nroom: str, num: int, maxnum: int):
    crooms.setdefault(num, {})
    crooms[num]['text'] = roomdata[nroom]['text']
    newnum = num
    roomdata[nroom].setdefault('choices', [])
    for choice in roomdata[nroom]['choices']:
        if newnum < maxnum:
            newnum += 1
            crooms[num].setdefault('choices', {})
            ranroom = random.choice(roomdata[nroom]['proutes'][choice])
            crooms[num]['choices'][choice] = newnum
            newnum = gen(crooms, roomdata, ranroom, newnum, maxnum)
    return newnum


name = input('What\'s gonna be the name of your cartridge? (str) ') or 'invalid name'
try:
    roomint = int(input('how many rooms would you like to be in your cartridge (not including the starter room)? (int) '))
except ValueError:
    roomint = 20
print('opening rooms.json...')
with open(os.path.abspath(os.getcwd()) + '/../Data/rooms.json') as f:
    roomdata = json.loads(f.read())

print('will generate rooms now...')
starterroom = random.choice(roomdata['srooms'])
crooms = {}
gen(crooms, roomdata, starterroom, 0, roomint)

with open(os.path.abspath(os.getcwd()) + '/' + name + '.json', 'w') as f:
    f.write(json.dumps(crooms))
print('Done!')
