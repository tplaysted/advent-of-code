import sys

input_path = 'input.txt'
sys.setrecursionlimit(10000)

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')[:-1]
n = len(lines[0])
grid = [[x for x in line] for line in lines]
adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

start, end = (0,0), (0, 0)

for i in range(n):  # find the start / end point
    for j in range(n):
        if grid[i][j] == 'S':
            start = (i, j)

        if grid[i][j] == 'E':
            end = (i, j)

nodes = {}

def search(i, j, depth):  # mark out distance from start along track
    nodes[(i, j)] = depth
    grid[i][j] = str(depth)

    for a in adj:
        if grid[i+a[0]][j+a[1]] == '.' or grid[i+a[0]][j+a[1]] == 'E':
            search(i+a[0], j+a[1], depth+1)

search(start[0], start[1], 0)

def postman_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

max_cheat = 20
max_time = nodes[end]

def time_saved(a, b):  # time saved by going straight there
    cheat_dist = postman_distance(a, b)
    fair_dist = nodes[b] - nodes[a]

    if cheat_dist < fair_dist:
        return fair_dist - cheat_dist

    return 0

def reachable(p, dist):  # diamond of radius dist
    r = {}

    for i in range(-dist, dist + 1):
        if p[0] + i < 0 or p[0] + i > n:
            continue

        for j in range(-dist, dist + 1):
            if p[1] + j < 0 or p[1] + j > n:
                continue

            if postman_distance(p, (p[0] + i, p[1] + j)) <= dist:
                r[(p[0] + i, p[1] + j)] = postman_distance(p, (p[0] + i, p[1] + j))

    return r

cheats = {}

for i in range(1, max_cheat + 1):
    print(i)
    for snode in nodes:
        reach = reachable(snode, i)  # cut down the nodes we search over

        for enode in reach:
            if enode not in nodes:
                continue

            if (snode, enode) in cheats:
                continue

            if postman_distance(snode, enode) <= i:
                cheats[(snode, enode)] = time_saved(snode, enode)

print(sum([1 for c in cheats if cheats[c] >= 100]))
