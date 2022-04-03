def graph2d():
    #number of nodes
    x=int(input())
    matrix={}
    for _ in range(x):
        #name of nodes
        i=int(input())
        matrix[i]=[]
    y=int(input())
    for i in range(y):
        #connections
        a=list(map(int,input().split()))
        matrix[a[0]].append(a[1])
        matrix[a[1]].append(a[0])
    return(matrix)

def bfs_haspath(matrix):
    #starting node
    snode=int(input())
    #ending node
    dnode=int(input())
    sn=[(snode)]
    res=[]
    while(sn):
        #print(sn,res)
        x=sn.pop(0)
        if x not in res:
            sn.extend(matrix[x])
            res.append(x)
    print(int(dnode in res))
        
x=graph2d()
bfs_haspath(x)
    