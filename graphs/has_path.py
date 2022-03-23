
def graph2d():
    x=int(input("how many vertices does the graph have?\n: "))
    matrix=[]
    for i in range(x):
        matrix.append([])
        adj=list(map(int,(input("what nodes are reachable from node number %d (use space to seperate them)?\n :"%(i+1)).split())))
        matrix[i]=adj
    return(matrix)

def bfs_haspath(matrix):
    snode=int(input("what is the starting node:-  "))
    dnode=int(input("what is the destination node:-  "))
    sn=[(snode)]
    res=[]
    while(sn):
        print(sn,res)
        x=sn.pop(0)
        if x not in res:
            sn.extend(matrix[x-1])
            res.append(x)
    print(dnode in res)
        
x=graph2d()
bfs_haspath(x)
    
