input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')

def from_grid(grid):
    return tuple(sum([grid[i][j] == '#' for i in range(7)]) - 1 for j in range(5))

keys, locks, i = set(), set(), 0

while i < len(lines) - 1:
    if lines[i] == '#####':
        locks.add(from_grid(lines[i:i+7]))

    if lines[i] == '.....':
        keys.add(from_grid(lines[i:i+7]))

    i += 8

def fits(lock, key):
    return all(lock[i] + key[i] < 6 for i in range(5))

total = 0

for lock in locks:
    for key in keys:
        if fits(lock, key):
            total += 1

print(total)
