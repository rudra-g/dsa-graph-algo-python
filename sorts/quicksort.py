def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    a=0
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            a=arr[j]
            arr[j]=arr[i]
            arr[i]=a
    a=arr[high]
    arr[high]=arr[i+1]
    arr[i+1]=a
    return i+1

def quick(arr,low,high):
    if (low<high):
        pivotindex=partition(arr,low,high)
        quick(arr,low,pivotindex-1)
        quick(arr,pivotindex+1,high)

def quicksort(arr):
    quick(arr,0,len(arr)-1)


a=[10,9,8,7,6,5,4,3,2,1]
quicksort(a)
print(a)
