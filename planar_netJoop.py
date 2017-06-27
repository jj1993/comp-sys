
# coding: utf-8

# In[ ]:
import numpy as np
import networkx as nx
from scipy.spatial import Delaunay
import random
    
def find_neighbors(pindex, triang):
    return triang.vertex_neighbor_vertices[1][triang.vertex_neighbor_vertices[0][pindex]:triang.vertex_neighbor_vertices[0][pindex+1]]

def createplanar(num):
    
    points=[]
    for i in range(95):
        points.append((np.random.uniform(0,1000),np.random.uniform(0,1000)))   
    point=np.array(points)
    tri = Delaunay(point)
    
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
    dif=nx.number_of_edges(G)-num
    edges=G.edges()
    
    keys=list(nx.degree(G,nx.nodes(G)).keys())
    degrees = list(nx.degree(G, nx.nodes(G)).values())
    degreesP = np.array(degrees, dtype=np.float)
    sumD = np.sum(degreesP)
    degreesP = degreesP / sumD

    i=0

    while dif>0:
        rnode=np.random.choice(keys, 1, replace=True, p=degreesP)[0]
        rnd=random.randint(0,len(G.edges(rnode))-1)
        edge=G.edges(rnode)[rnd]
        if nx.degree(G,edge[0])>1 and nx.degree(G,edge[1])>1:
            G.remove_edge(edge[0],edge[1])
            if not nx.is_connected(G):
                G.add_edge(edge[0],edge[1])
                dif+=1
            dif-=1
        i+=1
        if i>10000:
            break
    
    
    #print(nx.info(G))
    
    #print('custer=',nx.average_clustering(G))
    #print('custer=',nx.average_clustering(G))
    #print(nx.average_shortest_path_length(G))
    
    edges=[]
    edg=G.edges()
    
    for i in range(0,len(edg)):
        edges.append([tuple(point[edg[i][0]]),tuple(point[edg[i][1]])])
        
    return edges

