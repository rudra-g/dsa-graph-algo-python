def mul(li,x,y):
    return ((li[x]-li[y])*(x-y))

def swap(li,x,y):
    a=li[x]
    li[x]=li[y]
    li[y]=a
    return li

def choose(li):
    pass


num=int(input())

for i in range(num):
    n,k=map(int,str(input()).split())
    l=list(map(int,str(input()).split()))
    op=[]
    for j in range(k):
        op.append(list(map(int,str(input()).split())))
    print(num,n,k,l,op)
