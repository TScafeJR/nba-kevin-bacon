import networkx as nx
from netwulf import visualize

with open('src/data/graph.gml', 'r') as file:
    graph_file = file.read()

G = nx.parse_gml(graph_file)

visualize(G)