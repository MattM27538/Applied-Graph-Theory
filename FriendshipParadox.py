# File: FriendshipParadox.py
# Author: Matthew Martinez
# Description: File reads in edges for nodes from specified input file, creates a
# graph with the data, and creates a scatterplot plotting node degrees against mean
# neighbor node degree

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Function: read_Data_From_File()
# Description: Function
# Parameters: N/A
# Returns: class Graph
def read_Data_From_File():
    file1 = open("uc_irvine_network.edgelist", "r")
    friendshipGraph = nx.Graph()

    # Parse lines from file and edges to graph ignoring time stamps and 
    # using first and second ints of each line. Function returns resulting graph.
    for line in file1:
        l = line.split(' ')
        node1 = int(l[3])
        node2 = int(l[2])

        friendshipGraph.add_edge(node1,node2)
    return friendshipGraph

# Function: neighborDegrees()
# Description: Function returns mean of neighboring nodes' degrees.
# Parameters: friendshipParadoxGraph,v
# Returns: int
def neighborDegrees(friendshipParadoxGraph,v):
    listOfDegrees = [friendshipParadoxGraph.degree[u] for u in friendshipParadoxGraph.neighbors(v)]
    return np.mean(listOfDegrees)


def main():
    friendshipParadoxGraph = read_Data_From_File()
    nodes = sorted(friendshipParadoxGraph.nodes())

    degrees = [friendshipParadoxGraph.degree[v] for v in nodes]
    
    neighbors = [neighborDegrees(friendshipParadoxGraph,v) for v in nodes]

    plt.scatter(degrees,neighbors,alpha=0.5)
    plt.savefig("FriendshipParadoxGraph.png")

if __name__=="__main__": 
    main() 




