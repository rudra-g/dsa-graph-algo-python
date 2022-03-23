n=int(input())
for i in range(n):
    l=list(map(int, input().split()))
    sen=str(input())
    dog=sen.count("D")
    cat=sen.count("C")
    num=l[0]
    df=l[1]
    cf=l[2]
    ad=l[3]
    res=0
    for j in range(num):
        if ((df==0) and dog>0):
            break
        if sen[j]=="C":
            cf-=1
            cat-=1
        elif sen[j]=="D":
            df-=1
            cat+=ad
            dog-=1
        if (dog==0):
            res=1
            break
        if (cf<0) or (df<0):
            break
    if res==1:
        print("Case #"+str(i+1)+": YES")
    else:
        print("Case #"+str(i+1)+": NO")
