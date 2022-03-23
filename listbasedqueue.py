class que:
    def __init__(self,l) -> None:
        self.queue=l
        self.length=len(l)
    def show(self):
        for i in self.queue:
            print(i,end=" ")
        print("")
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def contains(self,x):
        if x in self.queue:
            return True
        else:
            return False
    def delete(self,y):
        if self.contains(y):
            self.queue.remove(y)
        else:
            print("element not in list")
    

    


x=que([1,2,3,4,5])
x.show()
x.enqueue(7)
x.show()
x.dequeue()
x.show()
x.delete(3)
x.show()
x.peek()

