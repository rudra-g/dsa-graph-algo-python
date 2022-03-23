class Node:
    def __init__(self,value=None,left=None,right=None) -> None:
        self.value=value
        self.left=left
        self.right=right

class BST:
    def __init__(self) -> None:
        self.root=None
        self.length=0

    def insert(self,value=None,left=None,right=None) -> None:
        new=Node(value,left,right)
        if (self.root):
            current=self.root
            if(current.value>new.value):
                while(current.value>new.value and current.left):
                    current=current.left
                while(current.value<new.value and current.right):
                    current=current.right
                if(current.value>new.value):
                    current.left=new
                else:
                    current.right=new
            if(current.value<new.value):
                while(current.value<new.value and current.right):
                    current=current.right
                while(current.value>new.value and current.left):
                    current=current.left
                if(current.value>new.value):
                    current.left=new
                else:
                    current.right=new

        else:
            self.root=new
        self.length+=1


    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.value,end="->")
            self.inorder(node.right)

    def showinorder(self):
        node=self.root
        self.inorder(node)
        print("None")

h=BST()
h.insert(5)
h.insert(4)
h.insert(3)
h.insert(2)
h.insert(1)
h.insert(6)
h.insert(7)
h.insert(8)
h.insert(9)
h.showinorder()

        
