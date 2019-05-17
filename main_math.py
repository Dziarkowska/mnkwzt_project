# Python program to find maximum number of edge disjoint paths 
# Complexity : (E*(V^3)) 
# Total augmenting path = VE 
# and BFS with adj matrix takes :V^2 times 

from collections import defaultdict 
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import argparse

def parseMatrix(numpy_matrix, num_of_nodes):
    matrix = numpy_matrix.astype(int)
    output = matrix.tolist()
    
    return output

def show_graph_with_labels(adjacency_matrix):
    fig=plt.figure()
    G2 = nx.from_numpy_matrix(np.array(adjacency_matrix), create_using=nx.MultiDiGraph())
    nx.draw(G2, with_labels=True)
    plt.show()

#This class represents a directed graph using 
# adjacency matrix representation 
class Graph: 

    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self. ROW = len(graph) 
        

    '''Returns true if there is a path from source 's' to sink 't' in 
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent): 

        # Mark all the vertices as not visited 
        visited =[False]*(self.ROW) 
        
        # Create a queue for BFS 
        queue=[] 
        
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
        
        # Standard BFS Loop 
        while queue: 

            #Dequeue a vertex from queue and print it 
            u = queue.pop(0) 
        
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u
                
        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
            
    
    # Returns tne maximum number of edge-disjoint paths from 
    #s to t in the given graph 
    def findDisjointPaths(self, source, sink): 

        # This array is filled by BFS and to store path 
        parent = [-1]*(self.ROW) 

        max_flow = 0 # There is no flow initially 

        # Augment the flow while there is path from source to sink 
        while self.BFS(source, sink, parent) : 

            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink
            que = [s] 
            while(s != source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
                que.append(s)
            print(str(que))
            # Add path flow to overall flow 
            max_flow += path_flow 

            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink
            while(v != source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
        return max_flow 

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file',
    help='Path to .GML file')
parser.add_argument('-si', '--sink',
    help='ID of sink node')
parser.add_argument('-so', '--source',
    help='ID of source node')
args = vars(parser.parse_args())

graph = nx.read_gml(args['file'])
print(graph.number_of_nodes())
print(graph.number_of_edges())



adj_matrix = parseMatrix(nx.to_numpy_matrix(graph), graph.number_of_nodes())
g = Graph(adj_matrix)
temp_matrix_to_draw = adj_matrix
#print(adj_matrix)
print("\n\n")

source = int(args['source'])
sink = int(args['sink'])


print ("There can be maximum %d edge-disjoint paths from %s to %s" %
           (g.findDisjointPaths(source, sink), source, sink)) 


show_graph_with_labels(adj_matrix)
input('Press Enter to exit')