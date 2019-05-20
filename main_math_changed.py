# Python program to find maximum number of edge disjoint paths 
# Complexity : (E*(V^3)) 
# Total augmenting path = VE 
# and BFS with adj matrix takes :V^2 times 

from collections import defaultdict 
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import argparse
import math
import sys

costs=[]
paths_list=[]

def parseMatrix(numpy_matrix, num_of_nodes):
    matrix = numpy_matrix.astype(int)
    output = matrix.tolist()
    return output

def show_graph_with_labels(adjacency_matrix):
    fig=plt.figure()
    G2 = nx.from_numpy_matrix(np.array(adjacency_matrix), create_using=nx.MultiDiGraph())
    nx.draw(G2, with_labels=True)
    plt.show()

#WSTĘP DO SPRAWDZANIA ROZŁĄCZNOŚCI WIERZCHOŁKOWEJ
def listsDiff(list1):
    if len(list1)>1:
        for l1 in list1:
            for l2 in list1:
                if l1 != l2:
                    li1 = (l1['path'])
                    li2 = (l2['path'])
                    st = [l1['path'][0],l1['path'][-1]]
                    diff = list((set(li1)&set(li2))-set(st))
                    if len(diff)!=0:
                        pass
# TO BE CONTINUED -> jeśli dwie ścieżki zawierają taką samą krawędź, wybieramy tą o niższym koszcie, tą o wyższym odrzucamy

#It choose the paths with the lowest cost
def print2Smallest(arr): 
   
    arr_size = len(arr) 
    first = second = sys.maxint 
    if arr_size >= 2: 
        first_path=paths_list[0]['path']
        second_path=paths_list[0]['path']
        for i in range(0, arr_size): 
    # If current element is smaller than first then 
    # update both first and second 
            if arr[i] < first: 
                second = first 
                first = arr[i] 
                first_path=paths_list[i]['path']
    # If arr[i] is in between first and second then 
    # update second 
            elif (arr[i] < second and arr[i] != first): 
                second = arr[i]
                second_path=paths_list[i]['path']
            elif (arr[i] < second and arr[i]==first):
                second = first
                second_path=paths_list[i]['path']
        print 'The lowest cost ({}) is the cost of path: {}'.format(first,first_path)
        print 'The second lowest cost({}) is the cost of path: {}\n'.format(second,second_path)     

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
            paths={}
            path_flow = float("Inf")
            s = sink
            que = [s] 
            while(s != source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
                que.append(s)
            
            nodes = graph.nodes.data()
            i=0
            nodes_list=[]
            for node in nodes:
                nodes_info={}
                nodes_info['id']=i
                nodes_info['name']=node[0]
                nodes_info['Latitude']=node[1]['Latitude']
                nodes_info['Longitude']=node[1]['Longitude']
                nodes_list.append(nodes_info)
                i+=1
            cost=0
            for num1 in range(len(que)):
                if num1!=len(que)-1:
                    cost=cost+10*math.acos(math.sin(nodes_list[num1]['Latitude'])*math.sin(nodes_list[num1+1]['Latitude'])+math.cos(nodes_list[num1]['Latitude'])*math.cos(nodes_list[num1+1]['Latitude'])*math.cos(nodes_list[num1]['Longitude']-nodes_list[num1+1]['Longitude']))
                    cost=int(cost)
            paths['cost']=cost
            paths['path']=que
            paths_list.append(paths)
            costs.append(cost)

            print(str(que))
            # Add path flow to overall flow 
            #max_flow += path_flow 
            max_flow+=1
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
args = vars(parser.parse_args())

graph = nx.read_gml(args['file'])
print(graph.number_of_nodes())
print(graph.number_of_edges())



adj_matrix = parseMatrix(nx.to_numpy_matrix(graph), graph.number_of_nodes())
g = Graph(adj_matrix)
temp_matrix_to_draw = adj_matrix
#print(adj_matrix)
print("\n\n")


for i in range(1, graph.number_of_nodes()):
    for j in range(1, graph.number_of_nodes()):
        if i!=j:
            print ("There can be maximum %d disjoint paths from %s to %s" %
                (g.findDisjointPaths(i, j), i, j)) 
            listsDiff(paths_list)
            print2Smallest(costs)
            del costs[0:len(costs)]
            del paths_list[0:len(paths_list)]


show_graph_with_labels(adj_matrix)

input('Press Enter to exit')
