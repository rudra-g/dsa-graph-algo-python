def insertion(li):
    key=None
    for i in range(0,len(li)):
        key=li[i]
        j=i-1
        while(j>=0 and li[j]>key):
            li[j+1]=li[j]
            j-=1
        li[j+1]=key

lis=[5,4,3,2,1]
insertion(lis)
print(lis)

