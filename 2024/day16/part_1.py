import networkx as nx

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
lines.pop()

height = len(lines)
width = len(lines[0])

G = nx.DiGraph()

dirs = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

for i in range(1, height-1):  # first pass adding nodes
    for j in range(1, width-1):
        if lines[i][j] == '#':
            continue

        [G.add_node((i, j, d)) for d in dirs]

edges = []

for i, j, d in G.nodes():  # second pass adding adjancencies
    next = lines[i + dirs[d][0]][j + dirs[d][1]]

    if next != '#':  # moving in a straight line
        edges += [((i, j, d), (i + dirs[d][0], j + dirs[d][1], d), 1)]

    if d == 'N' or d == 'S':  # turning
        edges += [((i, j, d), (i, j, 'W'), 1000), ((i, j, d), (i, j, 'E'), 1000)]
    else:
        edges += [((i, j, d), (i, j, 'N'), 1000), ((i, j, d), (i, j, 'S'), 1000)]

G.add_weighted_edges_from(edges)
shorts = [nx.dijkstra_path_length(G, (height-2, 1, 'E'), (1, width-2, d)) for d in dirs]
print(min(shorts))
