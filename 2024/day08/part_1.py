import re

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
lines = lines[0:len(lines)-1]

antennae = {}

for i, line in enumerate(lines):
    nodes = re.findall("[^.]", line)
    for node in nodes:
        cols = [i for i, x in enumerate(line) if x == node]
        if node in antennae:
            antennae.update({node: [(i, j) for j in cols] + antennae[node]})
        else:
            antennae.update({node: [(i, j) for j in cols]})

n = len(lines)

antinodes = [['.' for _ in range(n)] for _ in range(n)]

for a in antennae:
    pos = antennae[a]

    for i in range(len(pos) - 1):
        for j in range(i + 1, len(pos)):
            a = pos[i]  # first antennae
            b = pos[j]  # second antennae

            dist = (a[0] - b[0], a[1] - b[1])
            new_1 = (a[0] + dist[0], a[1] + dist[1])
            new_2 = (b[0] - dist[0], b[1] - dist[1])

            if new_1[0] > -1 and new_1[0] < n and new_1[1] > -1 and new_1[1] < n:
                antinodes[new_1[0]][new_1[1]] = '#'

            if new_2[0] > -1 and new_2[0] < n and new_2[1] > -1 and new_2[1] < n:
                antinodes[new_2[0]][new_2[1]] = '#'

total = 0

for i in range(n):
    for j in range(n):
        if antinodes[i][j] == '#':
            total += 1

print(total)
