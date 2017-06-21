import random
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def getDutchWeigthedNetwork():
    x = pd.read_csv("dutchhighway.csv", sep=';').values
    G = nx.Graph()
    G.add_nodes_from(x[:, 0])
    edges = []
    for i in range(len(x)):
        e = (x[i, 0], x[i, 1], x[i, 2])
        edges.append(e)
    G.add_weighted_edges_from(edges)
    return G


def getStats(G):
    degrees = list(nx.degree(G).values())
    print(nx.info(G))
    print("Path length:", nx.average_shortest_path_length(G), "expected:",
          np.log(nx.number_of_nodes(G)) /
          np.log(np.mean(nx.degree(G).values())))
    print("clustering coefficient:", nx.average_clustering(G), "expected:",
          np.mean(degrees) / nx.number_of_nodes(G))
    plt.plot(nx.degree_histogram(G))
    normDegrees = (degrees - np.mean(degrees)) / np.std(degrees)
    print("Excess kurtosis:", stats.kurtosis(normDegrees))


G = getDutchWeigthedNetwork()
getStats(G)
N = nx.number_of_nodes(G)
# you can vary clustering by varying p, and <k> will vary with it as well, as
# clustering in random graph is = p = <k> / N
p = np.mean(list(nx.degree(G).values())) / nx.number_of_nodes(G)
randG = nx.gnp_random_graph(N, p)
print(nx.info(randG))


#x = []
#numNodes = 95
#nodes = range(numNodes)
#degree = 3
#edges = int(0.5*degree*numNodes)
#p = 0.3
#while len(x) < edges:
#    n1 = random.choice(nodes)
#    n2 = random.choice(nodes)
#    if random.random() < p:
#        x.append([n1, n2, 0])
#x = np.array(x)


#print(nx.degree(G))

#plt.hist(list(nx.degree(G).values()))
#plt.show()
#plt.figure()
#nx.draw(G)
#plt.show()
#print(nx.average_shortest_path_length(G))