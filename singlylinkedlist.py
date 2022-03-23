class Node(object):
    def __init__(self,data=None,next_node=None) -> None:
        self.data=data
        self.next_node=next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self,new_next):
        self.next_node=new_next
    def set_data(self,data):
        self.data=data

def swapval(x,y):
    d=x.get_data()
    g=y.get_data()
    x.set_data(g)
    y.set_data(d)

def delnode(head,x):
    if head==x:
        head=x.get_next()
        del x
    else:
        g=head
        p=head.get_next()
        while(p!=x):
            g=p
            p=p.get_next()
        g.set_next(p.get_next())
        del x
        
def printlist(head):
    g=head
    print(g.get_data())
    while(g.get_next()!=None):
        g=g.get_next()
        print(g.get_data())    

x=Node(24)
y=Node(23)
z=Node(25)

head=x

swapval(x,y)
x.set_next(y)
y.set_next(z)

delnode(head,y)

printlist(head)
