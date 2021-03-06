#!/usr/bin/python

import networkx as nx
import sys
from operator import itemgetter
import math
nodes=[]
edges=[]
nodes_list=[]
edges_list=[]
G = nx.read_gml(sys.argv[1])
nodes=G.nodes.data()
edges=G.edges.data()
i=0
edges_number=len(edges)
nodes_number = len(nodes)
#
for node in nodes:
   nodes_info={}
   nodes_info['id']=i
   nodes_info['name']=node[0]
   nodes_info['Latitude']=node[1]['Latitude']
   nodes_info['Longitude']=node[1]['Longitude']
   nodes_list.append(nodes_info)
   i+=1


cost=0
for edge in edges:
   edges_info=[]
   edges_info.append(edge[0])
   edges_info.append(edge[1])   
   edges_info.append(int(edge[2]['id'][1:])+1)
   edges_list.append(edges_info)
   

for a in range(len(edges_list)):
  for b in range(2):
    for dicto in nodes_list:
      if edges_list[a][b]==dicto['name']:
        edges_list[a][b]=int(dicto['id'])+1
 
j=0
for edge in edges_list:
    cost=10*math.acos(math.sin(nodes_list[int(edge[0])-1]['Latitude'])*math.sin(nodes_list[int(edge[1])-1]['Latitude'])+math.cos(nodes_list[int(edge[0])-1]['Latitude'])*math.cos(nodes_list[int(edge[1])-1]['Latitude'])*math.cos(nodes_list[int(edge[0])-1]['Longitude']-nodes_list[int(edge[1])-1]['Longitude']))
    cost=int(cost)
    edges_list[j].append(cost)
    j+=1

sorted_edges_list=sorted(edges_list, key=lambda edges_list:edges_list[2])


print "data;\n## [number of nodes, arcs and demands]\nparam v := {};\nparam e := {};\nparam d := 1;\nparam m := 2;\n## [volume of demand, source node, destination node]\nparam : h  s t :=\n1       1 3 7;".format(nodes_number,2*edges_number)
print "\nparam : A :="
for i in range(edges_number):
    print "{:5} {:3}{:4}".format(i+1,sorted_edges_list[i][0],1)
for i in range(edges_number):
    if i!=edges_number-1:
        print "{:5} {:3}{:4}".format(i+edges_number+1,sorted_edges_list[i][1],1)
    else:
        print "{:5} {:3}{:4};".format(i+edges_number+1,sorted_edges_list[i][1],1)
	
print "\nparam : B :="
for i in range(edges_number):
    print "{:5} {:3}{:4}".format(i+1,sorted_edges_list[i][1],1)
for i in range(edges_number):
    if i!=edges_number-1:
        print "{:5} {:3}{:4}".format(i+edges_number+1,sorted_edges_list[i][0],1)
    else:
        print "{:5} {:3}{:4};".format(i+edges_number+1,sorted_edges_list[i][0],1)

print "\nparam : K :="
for i in range(edges_number):
    print "{:5} {:3}".format(i+1,sorted_edges_list[i][3])
for i in range(edges_number):
  if i!=(edges_number)-1:
    print "{:5} {:3}".format(i+edges_number+1,sorted_edges_list[i][3])
  else:
    print "{:5} {:3};".format(i+edges_number+1,sorted_edges_list[i][3])


print "\nend;"
