import json
import sys

with open('atlantis.json', 'r') as file:
    warps = json.load(file)

zone_from = {i: [] for i in range(1, 101)}
zone_to = {i: [] for i in range(1, 101)}
for warp in warps:
    zone_from[warp['to']].append(warp['from'])
    zone_to[warp['from']].append(warp['to'])

for i in range(1, 100):
    if len(zone_from[i]) == 1 and zone_from[i] == zone_to[i]:
        print(i, zone_from[i], zone_to[i])
