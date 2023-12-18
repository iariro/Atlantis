import json
import sys
import find_route

with open('atlantis.json', 'r') as file:
    warps = json.load(file)

major_route = (1, 2, 3, 4, 6, 8, 10, 25, 41, 94, 97)

with open('atlantis.md', 'w') as file:
    file.write('```mermaid\n')
    file.write('graph TD\n')
    for warp in warps:
        if warp['warp'] is not None:
            file.write('	{}({}) -- {} --> {}({})\n'.format(warp['from'], warp['from'], warp['warp'], warp['to'], warp['to']))
        else:
            file.write('	{}({}) --> {}({})\n'.format(warp['from'], warp['from'], warp['to'], warp['to']))
    file.write('    97(97) --> FINAL(FINAL)\n')
    file.write('    99(99) --> FINAL(FINAL)\n')
    file.write('    subgraph 最短ルート\n')
    for zone in major_route:
        file.write('    {}\n'.format(zone))
    file.write('    end\n')
    file.write('```\n')
