import numpy as np
import bigNetwork as bn
import matplotlib.pyplot as plt
from math import sqrt
import planar_netJoop as pn
import copy

M = 5  # number of monte carlo runs per network size
N = 5  # nr of network sizes
CLUST = np.linspace(0.05, .45, num=N)
AVG_SPEEDS_CLUST = np.empty((len(CLUST), M))
AVG_SPEEDS_CLUST_SP = np.empty((len(CLUST), M))
NW_SIZE = np.linspace(125, 215, num=N, dtype=int)  # size in nr of edges
AVG_SPEEDS = np.empty((len(NW_SIZE), M))  # simulation results
AVG_SPEEDS_NORM = np.empty((len(NW_SIZE), M))  # simulation results
DEGREES = 2. * NW_SIZE / 95


def main():
    # change clustering with degreeNrs constant at 145
    for i in range(N):
        for m in range(M):
            print(len(CLUST) - i, M - m)
            edges, G = pn.main(145, CLUST[i])
            AVG_SPEEDS_CLUST[i, m] =\
                bn.main(copy.deepcopy(edges), G, False, True)
            AVG_SPEEDS_CLUST_SP[i, m] =\
                bn.main(copy.deepcopy(edges), G, True, True)
            edges, G = pn.main(NW_SIZE[i], 0.11)  # function
            AVG_SPEEDS[i, m] = bn.main(copy.deepcopy(edges), G, True, False)
            AVG_SPEEDS_NORM[i, m] =\
                bn.main(copy.deepcopy(edges), G, True, True)
    plt.figure()
    plt.errorbar(CLUST, AVG_SPEEDS_CLUST.mean(axis=1),
                 AVG_SPEEDS_CLUST.std(axis=1) / sqrt(M), label="random path")
    plt.title("avg speed over clustering, nr of edges fixed at 145")
    plt.errorbar(CLUST, AVG_SPEEDS_CLUST_SP.mean(axis=1),
                 AVG_SPEEDS_CLUST_SP.std(axis=1) / sqrt(M),
                 label='shortest path')
    plt.title("avg speed over clustering, nr of edges fixed at 145")
    plt.legend()
    plt.xlabel('clustering coefficient')
    plt.ylabel('average speed')
    plt.show()
    plt.figure()
    plt.errorbar(DEGREES, AVG_SPEEDS.mean(axis=1),
                 AVG_SPEEDS.std(axis=1) / sqrt(M), label='not normalized')
    plt.title("avg speed over avg degree, clustering fixed at .11")
    plt.errorbar(DEGREES, AVG_SPEEDS_NORM.mean(axis=1),
                 AVG_SPEEDS_NORM.std(axis=1) / sqrt(M), label='normalized')
    plt.title("avg speed over avg degree, clustering fixed at .11")
    plt.legend()
    plt.xlabel('average degree')
    plt.ylabel('average speed')
    plt.show()


if __name__ == "__main__":
    main()
