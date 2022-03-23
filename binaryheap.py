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
    def show(self):
        print(self.heap)

class minheap():
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
        while(((a-1)//2>=0) and (self.heap[(a-1)//2]>self.heap[a])):
            x=self.heap[(a-1)//2]
            self.heap[(a-1)//2]=self.heap[a]
            self.heap[a]=x
            a=(a-1)//2
    def show(self):
        print(self.heap)


a=maxheap()
a.insert(1)
a.show()
a.insert(2)
a.show()
a.insert(3)
a.show()
a.insert(4)
a.show()
a.insert(5)
a.show()
a.insert(6)
a.show()

del a

a=minheap()
a.insert(1)
a.show()
a.insert(2)
a.show()
a.insert(3)
a.show()
a.insert(4)
a.show()
a.insert(5)
a.show()
a.insert(6)
a.show()




                