def findmin(li, start):
    x=start
    for i in range(start,len(li)):
        if li[i]<li[x]:
            x=i
    return x
def selectionsort(li):

    for i in range(len(li)):
        a=li[i]
        b=findmin(li,i)
        li[i]=li[b]
        li[b]=a
    return li

lis=[5,4,3,2,1]
selectionsort(lis)
print(lis)
