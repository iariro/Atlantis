import json
import sys
import find_route

with open('atlantis.json', 'r') as file:
    warps = json.load(file)

route_count = []

for i in range(2, 100):
    routes = find_route.find_route(warps, 1, i, [], 20)
    min_route = None
    for route in routes:
        if (min_route == None) or (len(route) < len(min_route)):
            min_route = route
    if min_route:
        print(i, min_route)
        route_count.append((len(min_route) if min_route else 0, i, min_route))

for count, zone, min_route in sorted(route_count):
    print('{:2} {:2} {}'.format(count, zone, ' '.join(('{:2}'.format(zone) for zone in min_route))))
