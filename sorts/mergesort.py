def mergesort(arr):
    if(len(arr)==1):
        return arr
    midpoint=len(arr)//2
    left=mergesort(arr[:midpoint])
    right=mergesort(arr[midpoint:])
    #print(left,right)
    arr=merge(left,right)
    #print(arr)
    return arr

def merge(arr1,arr2):
    arr=[]
    i=j=0
    while((i<len(arr1)) and (j<len(arr2))):
        if(arr1[i]<arr2[j]):
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    arr.extend(arr1[i:])
    arr.extend(arr2[j:])

    return arr

a=[10,9,8,7,6,5,4,3,2,1]
x=mergesort(a)
print(x)