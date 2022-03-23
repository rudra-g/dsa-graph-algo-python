# representing a graph as a 2d array

def graph2d():
    x=int(input("how many vertices does the graph have?\n: "))
    matrix=[]
    for i in range(x):
        matrix.append([])
        adj=list(map(int,(input("what nodes are reachable from node number %d (use space to seperate them)?\n :"%(i+1)).split())))
        matrix[i]=adj
    print(matrix)


#representing graph as a dictionary

def graphdict():
    x=int(input("how many vertices does the graph have?\n: "))
    graphd={}
    for i in range(x):
        adj=list(map(int,(input("what nodes are reachable from node number %d? (use space to seperate them)\n :"%(i+1)).split())))
        graphd[i]=adj
    print(graphd)

graphdict()