import gc
class Node():
    def __init__(self,value=None,prev_n=None,next_n=None) -> None:
        self.value=value
        self.prev=prev_n
        self.next=next_n

class doubly():
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def insert(self,value=None,prev_n=None,next_n=None):
        newNode=Node(value,prev_n,next_n)
        if(self.head):
            current=self.head
            while(current.next):
                current=current.next
            current.next=newNode
            newNode.prev=current
            self.tail=newNode
        else:
            self.head=newNode
            self.tail=newNode

    def delete(self,value):
        if(self.head):
            current=self.head
            if (current.value==value):
                self.head=current.next
                self.head.prev=None
                del current
                gc.collect()
            elif(self.tail.value==value):
                current=self.tail
                self.tail=current.prev
                self.tail.next=None
                gc.collect()
            else:
                while(current!=self.tail):
                    if(current.value==value):
                        prev=current.prev
                        nextn=current.next
                        prev.next=nextn
                        nextn.prev=prev
                        del current
                        gc.collect()
                        break
                    current=current.next
        else:
            print("empty linked list")

    def show(self):
        current=self.head
        while(current):
            print(current.value,end=" ")
            current=current.next
        print("")
    
    def showrev(self):
        current=self.tail
        while(current):
            print(current.value,end=" ")
            current=current.prev
        print("")

dll=doubly()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.delete(1)
dll.show()
dll.showrev()