import networkx as nx

with open('src/data/graph.gml', 'r') as file:
    graph_file = file.read()

G = nx.read_gml(graph_file)

graph_file.close()