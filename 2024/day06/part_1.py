import re

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
lines = [list(line) for line in lines]
height = len(lines) - 1
width = len(lines[0])

pos = [0, 0]

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if re.search("[\\^<>v]", c) is not None:
            pos = [i, j]
            dir = lines[i][j]

dirs = ['^', '>', 'v', '<']
lines[pos[0]][pos[1]] = 'X'

while True:
    if pos[0] == 0 and dir == '^':
        break

    if pos[0] == (height - 1) and dir == 'v':
        break

    if pos[1] == (width - 1) and dir == '>':
        break

    if pos[1] == 0 and dir == '<':
        break

    next = []
    right = '>'

    if dir == '^':
        next = [pos[0] - 1, pos[1]]
        right = '>'
    elif dir == '<':
        next = [pos[0], pos[1] - 1]
        right = '^'
    elif dir == '>':
        next = [pos[0], pos[1] + 1]
        right = 'v'
    elif dir == 'v':
        next = [pos[0] + 1, pos[1]]
        right = '<'

    if lines[next[0]][next[1]] == '#':
        dir = right
    else:
        lines[next[0]][next[1]] = 'X'
        pos = next

total = 0

for i in range(height):
    for j in range(width):
        if lines[i][j] == 'X':
            total += 1

print(total)
