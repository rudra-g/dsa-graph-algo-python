class maxheap():
    def __init__(self) -> None:
        self.heap=[]
        pass

    def insert(self,value):
        if self.heap:
            self.heap.append(value)
            self.shiftup()

        else:
            self.heap.append(value)
    
    def shiftup(self):
        a=len(self.heap)-1
        while(((a-1)//2>=0) and (self.heap[(a-1)//2]<self.heap[a])):
            x=self.heap[(a-1)//2]
            self.heap[(a-1)//2]=self.heap[a]
            self.heap[a]=x
            a=(a-1)//2

    def shiftdown(self):
        i=0
        x=0
        a=len(self.heap)-1
        while(a>=(i*2+1)):
            if (a>=(i*2+2)) and (max(self.heap[i],self.heap[i*2+2],self.heap[i*2+1])==self.heap[i]):
                break
            if (a>=(i*2+1)) and (max(self.heap[i],self.heap[i*2+1])==self.heap[i]):
                break
            if((a>=(i*2+2)) and (self.heap[i*2+2]>self.heap[i*2+1]) and (self.heap[i*2+2]>self.heap[i])):
                x=self.heap[i]
                self.heap[i]=self.heap[i*2+2]
                self.heap[i*2+2]=x
                i=i*2+2
            elif((a>=(i*2+1)) and (self.heap[i*2+1]>self.heap[i])):
                x=self.heap[i]
                self.heap[i]=self.heap[i*2+1]
                self.heap[i*2+1]=x
                i=i*2+1
    
    def heapify(self,l=None):
        for i in range(len(l)):
            self.insert(l[i])

    def poproot(self):
        a=self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap=self.heap[0:(len(self.heap))-1]
        self.shiftdown()
        return a
        
        


def heapsort(li):
    h=maxheap()
    h.heapify(li)
    for i in range(len(li)):
        li[i]=h.poproot()


a=[1,2,3,4,5,6,7,8,9,10]
heapsort(a)
print(a)
