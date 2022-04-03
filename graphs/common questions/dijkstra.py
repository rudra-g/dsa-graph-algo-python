from collections import defaultdict

#Initializing the Graph Class
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def addNode(self,value):
        self.nodes.add(value)
    
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

#Implementing Dijkstra's Algorithm
def dijkstra(graph, initial):
    visited = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    
    return visited

customGraph = Graph()
#number of nodes
a=int(input())
for i in range(a):
    #name of nodes
    x=input()
    customGraph.addNode(x)
#number of undirected edges
b=int(input())
for i in range(b):
    #undirected edges in the format v v edge_weight
    y=list(input().split())
    customGraph.addEdge(y[0],y[1],int(y[2]))
    #customGraph.addEdge(y[1],y[0],int(y[2]))
#starting node
snode=input()
#destination node
dnode=input()
z=(dijkstra(customGraph, snode))
if dnode in z:
    print(z[dnode])
else:
    print(-1)