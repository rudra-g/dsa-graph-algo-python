def graph2d():
    x=int(input("how many vertices does the graph have?\n: "))
    matrix=[]
    for i in range(x):
        matrix.append([])
        adj=list(map(int,(input("what nodes are reachable from node number %d (use space to seperate them)?\n :"%(i+1)).split())))
        matrix[i]=adj
    return(matrix)

def bfs(matrix,snode):
    sn=[(snode)]
    res=[]
    while(sn):
        #print(sn,res)
        x=sn.pop(0)
        if x not in res:
            sn.extend(matrix[x-1])
            res.append(x)
    return(res)
        
def ccomp(matrix):
    largest=[]
    res=0
    nodes=[0]*len(matrix)
    for i in range(len(matrix)):
        if nodes[i]==0:
            x=bfs(matrix,i+1)
            if len(largest)<len(x):
                largest=x.copy()
            for j in x:
                nodes[j-1]=1
            nodes[i]=1
            res+=1
    print("the number of connected components are:-\n"+str(res)+"\nthe largest component is:-\n"+str(largest))
        


x=graph2d()
ccomp(x)
    
