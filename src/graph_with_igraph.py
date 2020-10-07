import igraph as ig

G=ig.Graph.Read_GML('src/data/graph.gml')
labels=list(G.vs['label'])
N=len(labels)
E=[e.tuple for e in G.es]# list of edges
layt=G.layout('kk') #kamada-kawai layout
type(layt)