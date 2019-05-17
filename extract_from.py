#!/usr/bin/python

import networkx as nx
import sys
nodes=[]
edges=[]
nodes_list=[]
edges_list=[]
G = nx.read_gml(sys.argv[1])
nodes=G.nodes.data()
edges=G.edges.data()
i=0
for node in nodes:
   nodes_info={}
   nodes_info['id']=i
   nodes_info['name']=node[0]
   nodes_list.append(nodes_info)
   i+=1

for edge in edges:
   edges_info=[]
   edges_info.append(edge[0])
   edges_info.append(edge[1])   
   edges_list.append(edges_info)

for a in range(len(edges_list)):
  for b in range(2):
    for dicto in nodes_list:
      if edges_list[a][b]==dicto['name']:
        edges_list[a][b]=dicto['id']
 
used=[]
unique = [x for x in edges_list if x not in used and (used.append(x) or True)]

uniq_len = len(unique)
nodes_number = len(nodes_list)

AMatrix = [[0 for x in range(nodes_number)] for y in range(nodes_number)]

for i in range(uniq_len):
  AMatrix[unique[i][0]][unique[i][1]]=1
  AMatrix[unique[i][1]][unique[i][0]]=1

for i in range(nodes_number):
  print AMatrix[i]

