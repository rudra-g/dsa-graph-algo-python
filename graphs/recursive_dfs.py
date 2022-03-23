def graph2d():
    x=int(input("how many vertices does the graph have?\n: "))
    matrix=[]
    for i in range(x):
        matrix.append([])
        adj=list(map(int,(input("what nodes are reachable from node number %d (use space to seperate them)?\n :"%(i+1)).split())))
        matrix[i]=adj
    return(matrix)

def dfs(matrix):
    stnode=int(input("what is the starting node:-  "))
    visited=[]
    recdfs(matrix,stnode,visited)
    print(visited)
  
def recdfs(matrix,snode,visited):
    if snode not in visited:
        visited.append(snode)
        for i in matrix[snode-1]:
            recdfs(matrix,i,visited)

    

x=graph2d()
dfs(x)
    
