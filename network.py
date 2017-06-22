import random
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import scipy.stats as stats


def getDutchWeighted():
    x = pd.read_csv("dutchhighway.csv", sep=';', header=None).values
    G = nx.Graph(name="dutch highway network")
    nodes = np.append(x[:, 0], x[:, 1])
    nodes = np.unique(nodes)
    G.add_nodes_from(nodes)
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
          np.log(np.mean(list(nx.degree(G).values()))))
    print("clustering coefficient:", nx.average_clustering(G), "expected:",
          np.mean(degrees) / nx.number_of_nodes(G))
    plt.plot(nx.degree_histogram(G))
#    if np.std(degrees) != 0:
#        normDegrees = (degrees - np.mean(degrees)) / np.std(degrees)
#        print("Excess kurtosis:", stats.kurtosis(normDegrees))
#    else:
#        print("Zero standard deviation in the degrees")


def getErdosRenyi():
    G = getDutchWeighted()
    randG = nx.erdos_renyi_graph(nx.number_of_nodes(G),
                                 np.mean(nx.degree(G).values()) /
                                 nx.number_of_nodes(G))
    degrees = nx.degree(randG, nx.nodes(randG)).values()
    degreesP = np.array(degrees, dtype=np.float)
    sumD = np.sum(degreesP)
    degreesP = degreesP / sumD
    keys = nx.degree(randG, nx.nodes(randG)).keys()

    for node in nx.nodes_iter(randG):
        if nx.degree(randG, node) == 0:
            choice = np.random.choice(keys, 1, replace=True, p=degreesP)[0]
            randG.add_edge(node, choice)
    randG.remove_edges_from(randG.selfloop_edges())
    return randG


def getRegular():
    G = getDutchWeighted()
    regG = nx.random_regular_graph(3, nx.number_of_nodes(G), seed=None)
    return regG


def getWS():
    G = getDutchWeighted()
    wsG = nx.connected_watts_strogatz_graph(96, 4, .3, tries=100, seed=None)
    dif = nx.number_of_edges(wsG) - nx.number_of_edges(G)
    edges = wsG.edges()
    random.shuffle(edges)
    i = 0
    while dif > 0:
        edge = edges[i]
        if nx.degree(wsG, edge[0]) > 1 and nx.degree(wsG, edge[0]) > 1:
            wsG.remove_edge(edge[0], edge[1])
            dif -= 1
        i += 1
    return wsG

G = getWS()
getStats(G)
getStats(getDutchWeighted())

#randG = 
#getStats(randG)


#N = nx.number_of_nodes(G)
## you can vary clustering by varying p, and <k> will vary with it as well, as
## clustering in random graph is = p = <k> / N
#p = np.mean(list(nx.degree(G).values())) / nx.number_of_nodes(G)
#
#randG = nx.random_regular_graph(np.mean(nx.degree(G).values()), 95)
#
#getStats(randG)

#make connected!


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