# this is python 2.7

import networkx as nx
import pandas as pd
#import matplotlib.pyplot as plt

x = pd.read_csv("dutchhighway.csv", sep=';').values

G = nx.Graph()
G.add_nodes_from(x[:, 0])

edges = []
for i in range(len(x)):
    e = (x[i, 0], x[i, 1], x[i, 3])
    edges.append(e)

G.add_weighted_edges_from(edges)

#print "nr of nodes:", len(G.nodes())
#print "nr of edges:", len(G.edges())
#
#print "clustering coefficient:", nx.average_clustering(G)

#print nx.degree(G)

#plt.hist(nx.degree(G).values())
nx.draw(G)

print nx.average_shortest_path_length(G)