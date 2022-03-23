def graph2d():
    x=int(input("how many vertices does the graph have?\n: "))
    matrix=[]
    for i in range(x):
        matrix.append([])
        adj=list(map(int,(input("what nodes are reachable from node number %d (use space to seperate them)?\n :"%(i+1)).split())))
        matrix[i]=adj
    return(matrix)

def dfs(matrix):
    snode=int(input("what is the starting node:-  "))
    sn=[(snode)]
    res=[]
    while(sn):
        print(sn,res)
        x=sn.pop()
        if x not in res:
            sn.extend(matrix[x-1])
            res.append(x)
    print(res)
        
x=graph2d()
dfs(x)
    
