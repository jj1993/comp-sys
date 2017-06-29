import numpy as np
import networkx as nx
from scipy.spatial import Delaunay
import random
import matplotlib.pyplot as plt
from collections import OrderedDict
    
def find_neighbors(pindex, triang):
    return triang.vertex_neighbor_vertices[1][triang.vertex_neighbor_vertices[0][pindex]:triang.vertex_neighbor_vertices[0][pindex+1]]

def main(num, clCoef):
    clCoef += 0.0025
    points=[]
    for i in range(95):
        points.append((np.random.uniform(0,1000),np.random.uniform(0,1000)))   
    point=np.array(points)
    tri = Delaunay(point)
    points = tri.points
#    plt.triplot(point[:,0], point[:,1], tri.simplices)
#    plt.plot(point[:,0], point[:,1], 'o')
#    plt.show()
    edges = []
    distances = []
    for i in range(len(tri.points)):
        neighbors = find_neighbors(i, tri)
        for j in neighbors:
            if j < i:
                edges.append((i, j))
                distances.append(np.sqrt((points[j, 0] - points[i, 0])**2 +
                                         (points[j, 1] - points[i, 1])**2))
    G = nx.Graph()

    for i in range(len(tri.points)):
        G.add_node(i, pos=tuple(points[i]))

    for i in range(len(edges)):
        G.add_edge(edges[i][0], edges[i][1], length=distances[i])

    G.add_edges_from(edges)
    dif=nx.number_of_edges(G)-num
    edges=G.edges()
    
#    keys=nx.degree(G, nx.nodes(G))
#    degrees = list(nx.degree(G, nx.nodes(G)).values())
#    degreesP = np.array(degrees, dtype=np.float)
#    sumD = np.sum(degreesP)
#    degreesP = degreesP / sumD

#    print np.array(list(nx.degree(G, nx.nodes(G)).values())).mean()
    

    margin = 0.005
    i = 0
    while dif > 0:
        edges = G.edges()
        random.shuffle(edges)
        edge = edges[0]
        coef = nx.average_clustering(G)

        if nx.degree(G, edge[0]) > 1 and nx.degree(G, edge[1]) > 1:
            G.remove_edge(edge[0], edge[1])
            dif -= 1
            if coef > clCoef + margin:
                if nx.average_clustering(G) > coef or not nx.is_connected(G):
                    G.add_edge(edge[0], edge[1])
                    dif += 1
            elif coef < clCoef - margin:
                if nx.average_clustering(G) < coef or not nx.is_connected(G):
                    G.add_edge(edge[0], edge[1])
                    dif += 1
            elif not nx.is_connected(G):
                G.add_edge(edge[0], edge[1])
                dif += 1
        i += 1
#        if i % 100 == 0:
#            print i
        if i > 1000:
            main(num, clCoef)


#    nx.draw(G)
    

#    print(nx.info(G))
#    print('cluster=', nx.average_clustering(G))
#    print('avg length', nx.average_shortest_path_length(G))
    
    edges=[]
    edg=G.edges()
    
    for i in range(0,len(edg)):
        edges.append([tuple(point[edg[i][0]]),tuple(point[edg[i][1]])])
        
    return edges, G

if __name__ == "__main__":
    main(145, 0.15)

