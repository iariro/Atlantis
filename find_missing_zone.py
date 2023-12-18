import json
import sys
import find_route

with open('atlantis.json', 'r') as file:
    warps = json.load(file)

reach = {i: False for i in range(1, 100)}
for i in range(1, 100):
    if reach[i] == False:
        routes = find_route.find_route(warps, 1, i, [], 20)
        for route in routes:
            for zone in route:
                reach[int(zone)] = True

missing = [i for i, flag in reach.items() if flag == False]

for warp in warps:
    if int(warp['from']) in missing and int(warp['to']) in missing:
        print('	{}({}) --> {}({})'.format(warp['from'], warp['from'], warp['to'], warp['to']))
for zone in missing:
    print('    {}'.format(zone))
