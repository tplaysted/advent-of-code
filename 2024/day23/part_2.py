import networkx as nx  # yeah it's cheating, what're you gonna do

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

edges = [(x[0:2], x[3:5]) for x in input.split('\n')[:-1]]
G = nx.Graph()
G.add_edges_from(edges)

lan = max(list(nx.find_cliques(G)), key=lambda x: len(x))  # 3-cliques
print(','.join(sorted(lan)))
