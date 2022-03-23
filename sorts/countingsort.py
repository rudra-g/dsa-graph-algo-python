def counting(li):
    a=[0]*10
    b=[0]*len(li)
    for i in li:
        a[i]+=1
    #print(a)
    for i in range(1,len(a)):
        a[i]=a[i]+a[i-1]
    #print(a)
    for i in li:
        b[a[i]-1]=i
        a[i]-=1
    return b

lis=[5,4,3,2,1]
b=counting(lis)
print(b)
    