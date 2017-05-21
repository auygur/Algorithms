"""
The purpose of this project is to show how to handle graph data structures. I implemented depth-first search for identifying the connected components of an undirected graph, implementing procedure Search as a subroutine along the way. I used the NetworkX Python package to represent and manipulate graphs. I used Homer's Iliad to create my Graph nodes and edges.
"""
import networkx as nx
import urllib2
import itertools
homer = urllib2.urlopen('http://people.sc.fsu.edu/~jburkardt/datasets/sgb/homer.dat') #iniatilizing an instance
homer=homer.readlines() #Storing the instance above into a list

#Reading nodes in the graph, for a given list. You can also readlines() function inside read_nodes(), however it will require to re-call url afterwards.
def read_nodes(gfile):
    a, nodes=[],[] 

    for i in range(4,565):   #this can be done in a smarter way but I knew that each node is the first element of each line.
        a=gfile[i].split()
        c=a[0]
        nodes.append(c)   
    return sorted(nodes)

#Reading edges in the graph, for a given list.
def read_edges(gfile):
    edges=[]
    for i in range(566,len(gfile)-1):
        s = gfile[i].strip()
        for x in s.split(':')[1].split(';'):
            edges.extend(list(itertools.combinations(x.split(","),2)))
    return sorted(edges)

#Importing additional libraries to draw the graph.
%matplotlib inline
import matplotlib
import networkx as nx
G = nx.Graph()
G.add_nodes_from(read_nodes(homer))
G.add_edges_from(read_edges(homer))
nx.draw(G)

#Search funciton takes a graph and a vertex Root, and runs a DFS through a graph, starting a given root. Neighboring nodes are processed in alphabetical order.

def Search(graph, root):
    initial_deck, visited=[], []
    initial_deck.append(root)
    while initial_deck:
        vertex=initial_deck.pop(0) 
        if vertex not in visited:
            visited.append(vertex)
            initial_deck.extend(x for x in sorted(graph[vertex]) if x not in visited)
    return visited

#Checking correctess of the code by verifying that it correctly computes the DFS tree starting at Ulssess (node OD)
ulysses = Search(G, 'OD')
print len(ulysses),"\n"
ulysses

#Now implementing DFS to compute the connected components of the given graph.

def connected_components(graph):
    a, visited=sorted(graph.nodes()), []
    while len(a)!=0:
        nodes=Search(G,a[0])
        visited.append(nodes)
        for i in nodes:
            a.remove(i)
    return visited

print len(connected_components(G))
connected_components(G)

#Testing correctess
character_interactions = connected_components(G)
component_sizes = [len(c) for c in character_interactions]
print "There are 12 connected components in the Iliad:", len(component_sizes) == 12
print "The giant component has size 542:", max(component_sizes) == 542
print "There are 5 isolated characters:", len([c for c in component_sizes if c == 1]) == 5
