from collections import deque

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
lines.pop()

bytes = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in lines]
size = 71

# Looking for minimum distance, so do a bfs
def min_path_out(grid):
    visited  = {(0, 0)}
    queue = deque()
    queue.append((0, 0, 1))  # keep track of depth

    while queue:
        x, y, depth = queue.popleft()
        for i, j in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:

            if i < 0 or i >= size or j < 0 or j >= size:
                continue

            if grid[i][j] == '#':
                continue

            if (i, j) in visited:
                continue

            if i == size-1 and j == size-1:
                return depth

            visited.add((i, j))
            queue.append((i, j, depth+1))

    return -1

def search(min, max):  # do a binary search and save some time
    if min == max:
        return min

    centre = (min + max) // 2
    grid = [['.' for _ in range(size)] for _ in range(size)]

    for i in range(centre + 1):
        grid[bytes[i][1]][bytes[i][0]] = '#'  # column row order

    plen = min_path_out(grid)

    if plen == -1:  # no path out so centre >= ans
        return search(min, centre)
    else:  # path out so centre < ans
        return search(centre + 1, max)

print(','.join([str(x) for x in bytes[search(0, len(bytes)-1)]]))
