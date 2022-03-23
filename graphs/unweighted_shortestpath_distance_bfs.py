from attr import NOTHING


def graph2d():
    x=int(input("how many vertices does the graph have?\n: "))
    matrix=[]
    for i in range(x):
        matrix.append([])
        adj=list(map(int,(input("what nodes are reachable from node number %d (use space to seperate them)?\n :"%(i+1)).split())))
        matrix[i]=adj
    return(matrix)

def shortestpath_bfs(matrix):
    snode=int(input("what is the starting node:-  "))
    dnode=int(input("what is the destination node:-  "))
    num=0
    sn=[[(snode),num]]
    res=[]
    flag=[0,0]
    while(sn):
        num+=1
        x=sn.pop(0)
        if x[0] not in res:
            temp=matrix[x[0]-1]
            for k in temp:
                sn.append([k,num])
                if k==dnode:
                    flag=[k,num]
                    break
            res.append(x[0])
    print(flag)
        
x=graph2d()
shortestpath_bfs(x)
    
