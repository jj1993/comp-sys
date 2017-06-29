import numpy as np
import bigNetwork as bn
import matplotlib.pyplot as plt
from math import sqrt
import planar_netJoop as pn

M = 2  # number of monte carlo runs per network size
N = 2  # nr of network sizes
#  DO NOT PUT NW_SIZE TOO LOW BECAUSE IT IS GOING TO HANG
NW_SIZE = np.linspace(125, 215, num=N, dtype=int)  # size in nr of edges
AVG_SPEEDS = np.empty((len(NW_SIZE), M))  # simulation results
CLUST = np.linspace(0.05, .45, num=N)
AVG_SPEEDS_CLUST = np.empty((len(CLUST), M))
# DEGREES = NW_SIZE /


def main():
    # change clustering with degreeNrs constant at 145
    for i in range(N):
        for m in range(M):
            edges, G = pn.main(145, CLUST[i])
            print(len(CLUST) - i, M - m)
            AVG_SPEEDS_CLUST[i, m] = bn.main(edges, G, True)
            edges, G = pn.main(NW_SIZE[i], 0.11)  # function
            AVG_SPEEDS[i, m] = bn.main(edges, G, True)
    plt.errorbar(CLUST, AVG_SPEEDS_CLUST.mean(axis=1),
                 AVG_SPEEDS_CLUST.std(axis=1) / sqrt(M))
    plt.title("avg speed over clustering, number of edges fixed at 145")
    plt.show()
    plt.figure()
    plt.errorbar(NW_SIZE, AVG_SPEEDS.mean(axis=1),
                 AVG_SPEEDS.std(axis=1) / sqrt(M))
    plt.title("avg speed over number of edges, clustering fixed at .11")
    plt.show()


if __name__ == "__main__":
    main()
