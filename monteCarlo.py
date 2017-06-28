import numpy as np
import bigNetwork as bn
import matplotlib.pyplot as plt
from math import sqrt
import planar_netJoop as pn

M = 2  # number of monte carlo runs per network size
N = 5  # nr of network sizes
NW_SIZE = np.linspace(125, 165, num=N, dtype=int)  # size in nr of edges
AVG_SPEEDS = np.empty((len(NW_SIZE), M))  # simulation results
CLUST = np.linspace(0.05, .45, num=N)
AVG_SPEEDS_CLUST = np.empty((len(CLUST), M))


def main():

    # change clustering with degreeNrs constant at 145
    for i in range(N):
        for m in range(M):
            edges = pn.main(145, CLUST[i])
            print(len(CLUST) - i, M - m)
            AVG_SPEEDS_CLUST[i, m] = bn.main(edges)
            edges = pn.main(NW_SIZE[i], 0.11)  # function
            AVG_SPEEDS[i, m] = bn.main(edges)
    plt.errorbar(CLUST, AVG_SPEEDS_CLUST.mean(axis=1),
                 AVG_SPEEDS_CLUST.std(axis=1) / sqrt(M))
    plt.show()
    plt.figure()
    plt.errorbar(NW_SIZE, AVG_SPEEDS.mean(axis=1),
                 AVG_SPEEDS.std(axis=1) / sqrt(M))
    plt.show()


if __name__ == "__main__":
    main()
