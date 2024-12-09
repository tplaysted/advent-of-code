import re
from copy import deepcopy

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

slines = input.split('\n')
slines = [list(line) for line in slines]
height = len(slines) - 1
width = len(slines[0])

spos = [0, 0]
dir = ''

for i, line in enumerate(slines):
    for j, c in enumerate(line):
        if re.search("[\\^<>v]", c) is not None:
            spos = [i, j]
            dir = slines[i][j]

total = 0
slines[spos[0]][spos[1]] = '.'

for i in range(height):
    for j in range(width):
        pos = deepcopy(spos)
        dir = '^'
        lines = deepcopy(slines)

        if i == spos[0] and j == spos[1]:
            continue

        lines[i][j] = '#'

        print(i, j)

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
            elif lines[pos[0]][pos[1]] == dir:
                total += 1
                break
            else:
                lines[pos[0]][pos[1]] = dir
                pos = next



print(total)
