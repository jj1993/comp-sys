import numpy as np
import bigNetwork as bn
import matplotlib.pyplot as plt
from math import sqrt
import planar_netJoop as pn

M = 10  # number of monte carlo runs per network size
N = 6  # nr of network sizes
NW_SIZE = np.linspace(100, 200, num=N, dtype=int)  # size in nr of edges
AVG_SPEEDS = np.empty((len(NW_SIZE), M))  # simulation results


def main():
    for i in range(len(NW_SIZE)):
        for m in range(M):
            edges, G = pn.createplanar(NW_SIZE[i])  # function
            AVG_SPEEDS[i, m] = bn.main(edges, None)
            print(len(NW_SIZE) - i, M - m)
    plt.errorbar(NW_SIZE, AVG_SPEEDS.mean(axis=1),
                 AVG_SPEEDS.std(axis=1) / sqrt(M))
    plt.show()


if __name__ == "__main__":
    main()
