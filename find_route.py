
def find_route(warps, current, goal, past, limit):
    if len(past) > limit:
        return []
    if current == goal:
        yield [current]
    else:
        for warp in warps:
            if warp['from'] == current and warp['to'] not in past:
                for route in find_route(warps, warp['to'], goal, past + [current], limit):
                    yield [current] + route
