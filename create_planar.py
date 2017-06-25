import networkx as nx
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt



def find_neighbors(pindex, triang):
    return triang.vertex_neighbor_vertices[1][triang.vertex_neighbor_vertices[0][pindex]:triang.vertex_neighbor_vertices[0][pindex+1]]

def createplanar():
      points=[]
      for i in range(200):
          points.append((np.random.uniform(0,1000),np.random.uniform(0,1000)))
      point=np.array(points)
      tri = Delaunay(point)
      plt.triplot(point[:,0], point[:,1], tri.simplices)
      plt.plot(point[:,0], point[:,1], 'o')
      plt.show()
      edges=[]
      for i in range(len(tri.points)):
          neighbors=find_neighbors(i, tri)
          for j in neighbors:
              if j<i:
                  edges.append((i,j))
      G=nx.Graph()
      nodes=[]
      for i in range(len(tri.points)):
          nodes.append(i)
      G.add_nodes_from(nodes)
      G.add_edges_from(edges)
      clust=list(nx.clustering(G).values())
      deg=list(nx.degree(G).values())
      avclust=np.mean(clust)
      print('Clustering=',avclust)
      avdeg=np.mean(deg)
      print('Degree=',avdeg)
      return tri.points,edges

a,b=createplanar()
