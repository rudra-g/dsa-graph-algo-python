def bubble(li):
    for i in range(len(li)):
        for i in range(len(li)):
            if i!=0 and li[i]<li[i-1]:
                a=li[i-1]
                li[i-1]=li[i]
                li[i]=a

lis=[5,4,3,2,1]
bubble(lis)
print(lis)