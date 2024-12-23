import networkx as nx  # yeah it's cheating, what're you gonna do

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

edges = [(x[0:2], x[3:5]) for x in input.split('\n')[:-1]]
G = nx.Graph()
G.add_edges_from(edges)

cliques = [s for s in nx.enumerate_all_cliques(G) if len(s) == 3]  # 3-cliques

def has_t(clique):
    for node in clique:
        if node[0] == 't':
            return True

    return False

total = sum([1 for c in cliques if has_t(c)])
print(total)
