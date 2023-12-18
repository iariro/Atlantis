import json
import sys
import find_route

with open('atlantis.json', 'r') as file:
    warps = json.load(file)

routes = find_route.find_route(warps, 1, int(sys.argv[1]), [], int(sys.argv[2]))
count = 0
zones = []
for route in routes:
    zones += route
    count += 1
print('ルート数 {}'.format(count))

major_route = (1, 2, 3, 4, 6, 8, 10, 25, 41, 94, 97)

with open('atlantis.md', 'w') as file:
    file.write('```mermaid\n')
    file.write('graph TD\n')
    for warp in warps:
        if warp['from'] in zones and warp['to'] in zones:
            if warp['warp'] is not None:
                file.write('	{}({}) -- {} --> {}({})\n'.format(warp['from'], warp['from'], warp['warp'], warp['to'], warp['to']))
            else:
                file.write('	{}({}) --> {}({})\n'.format(warp['from'], warp['from'], warp['to'], warp['to']))
    if False:
        file.write('    97(97) --> FINAL(FINAL)\n')
        file.write('    99(99) --> FINAL(FINAL)\n')
        file.write('    subgraph 最短ルート\n')
        for zone in major_route:
            file.write('    {}\n'.format(zone))
        file.write('    end\n')
    file.write('```\n')
