# this is python 2.7
import random
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = pd.read_csv("dutchhighway.csv", sep=';').values

x = []
numNodes = 95
nodes = range(numNodes)
degree = 3
edges = int(0.5*degree*numNodes)
p = 0.3
while len(x) < edges:
    n1 = random.choice(nodes)
    n2 = random.choice(nodes)
    if random.random() < p:
        x.append([n1, n2, 0])
x = np.array(x)

G = nx.Graph()
G.add_nodes_from(x[:, 0])

edges = []
for i in range(len(x)):
    e = (x[i, 0], x[i, 1], x[i, 2])
    edges.append(e)

G.add_weighted_edges_from(edges)

print("nr of nodes:", len(G.nodes()))
print("nr of edges:", len(G.edges()))

print("clustering coefficient:", nx.average_clustering(G))

print(nx.degree(G))

plt.hist(list(nx.degree(G).values()))
plt.show()
nx.draw(G)
plt.show()

print(nx.average_shortest_path_length(G))
