import networkx as nx
import re

from functools import cache

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

codes = input.split('\n')[:-1]

numpad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [' ', '0', 'A']]
dirpad = [[' ', '^', 'A'], ['<', 'v', '>']]

n_pos = {numpad[i][j]: (i, j) for i in range(4) for j in range(3)}
d_pos = {dirpad[i][j]: (i, j) for i in range(2) for j in range(3)}

adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = nx.Graph()
D = nx.Graph()

for k, (i, j) in n_pos.items():
    if k == ' ':
        continue

    for a in adj:
        x, y = i + a[0], j + a[1]

        if not (0 <= x < 4 and 0 <= y < 3):
            continue

        if numpad[x][y] == ' ':
            continue

        N.add_edge((i, j), (i + a[0], j + a[1]))

for k, (i, j) in d_pos.items():
    if k == ' ':
        continue

    for a in adj:
        x, y = i + a[0], j + a[1]

        if not (0 <= x < 2 and 0 <= y < 3):
            continue

        if dirpad[x][y] == ' ':
            continue

        D.add_edge((i, j), (i + a[0], j + a[1]))

def steps(path):  # turns a sequence of n (i, j) nodes into a sequence of n dir keys <<>>^vvA etc
    steps = []
    for i in range(len(path) - 1):
        a, b = path[i], path[i+1]

        if a[0] == b[0] and a[1] == b[1] + 1:
            steps += ['<']

        if a[0] == b[0] and a[1] == b[1] - 1:
            steps += ['>']

        if a[0] == b[0] + 1 and a[1] == b[1]:
            steps += ['^']

        if a[0] == b[0] - 1 and a[1] == b[1]:
            steps += ['v']

    return steps + ['A']

def postman_dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

@cache
def presses_d(a, b, depth): # no. key presses required to press B starting at A at a given depth (no. bots)
    if depth == 0:
        return postman_dis(d_pos[a], d_pos[b]) + 1

    min_cost = float('inf')

    for path in nx.all_shortest_paths(D, d_pos[a], d_pos[b]):
        arrows = steps(path)
        cost = presses_d('A', arrows[0], depth - 1)

        for i in range(len(arrows) - 1):
            x, y = arrows[i], arrows[i+1]
            cost += presses_d(x, y, depth - 1)

        if cost < min_cost:
            min_cost = cost

    return min_cost

def presses_n(a, b, depth): # key presses required to press B starting at A (on numpad) at a given depth (no. bots)
    if depth == 0:
        return postman_dis(n_pos[a], n_pos[b]) + 1

    min_cost = float('inf')

    for path in nx.all_shortest_paths(N, n_pos[a], n_pos[b]):
        arrows = steps(path)
        cost = presses_d('A', arrows[0], depth - 1)

        for i in range(len(arrows) - 1):
            x, y = arrows[i], arrows[i+1]
            cost += presses_d(x, y, depth - 1)

        if cost < min_cost:
            min_cost = cost

    return min_cost

def complexity(code, depth):
    n = int(re.findall('(\\d+)A', code)[0])
    presses = presses_n('A', code[0], depth)

    for i in range(len(code) - 1):
        a, b = code[i], code[i+1]
        presses += presses_n(a, b, depth)

    return n * presses

total = sum([complexity(code, 25) for code in codes])
print(total)
