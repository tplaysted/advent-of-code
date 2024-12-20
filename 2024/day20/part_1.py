from collections import deque

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')[:-1]
n = len(lines[0])
grid = [[x for x in line] for line in lines]
adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

nodes = {(i, j) for i in range(n) for j in range(n) if grid[i][j] != '#'}
walls = [(i, j) for i in range(1, n-1) for j in range(1, n-1) if grid[i][j] == '#']

start, end = (0,0), (0,0)

for node in nodes:
    if grid[node[0]][node[1]] == 'S':
        start = node

    if grid[node[0]][node[1]] == 'E':
        end = node

def time(wall):  # breadth first search again
    old = grid[wall[0]][wall[1]]
    grid[wall[0]][wall[1]] = "."
    visited  = {start}
    queue = deque()
    queue.append((start[0], start[1], 1))  # keep track of depth

    while queue:
        x, y, depth = queue.popleft()
        for i, j in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
            if i < 0 or i >= n or j < 0 or j >= n:
                continue

            if grid[i][j] == '#':
                continue

            if (i, j) in visited:
                continue

            if i == end[0] and j == end[1]:
                grid[wall[0]][wall[1]] = old  # reset grid
                return depth

            visited.add((i, j))
            queue.append((i, j, depth+1))

    grid[wall[0]][wall[1]] = old  # reset grid
    return -1

cheats = []
fair_time = time((0, 0))
for w in walls:
    near = [(w[0]+a[0], w[1]+a[1]) for a in adj if grid[w[0]+a[0]][w[1]+a[1]] != "#"]

    if len(near) < 2:
        continue

    time_saved = fair_time - time(w)

    if time_saved >= 100:
        cheats += [(w, time_saved)]

print(len(cheats))
