#Define a class
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def display(self):
        if self.left :
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()

    def Insert(self,data):
        if self.data: # if root is none

            if self.data > data:   # for left 
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.Insert(data)
             
            if self.data < data:    #for right
                if self.right is None:
                    self.right = Node(data) 
                else:
                    self.right.Insert(data)
        
        else:
            self.data = data
                  
    def search(self,value):
        if self.data == value:
            return True
        elif self.data > value:
            if self.left is None:
                return False
            return self.left.search(value)
        elif self.data < value:
            if self.right is None:
                return False
            return self.right.search(value)
    
   #inorder left--> root--> right

    def inorder(self, root):
        result = []
        if root:
            result = self.inorder(root.left)
            result.append(root.data)
            result =  result + self.inorder(root.right)
        return result

     #postorder left--> right --> root
    def postorder(self, root):
        result = []
        if root:
            result = self.inorder(root.left)
            result =  result + self.inorder(root.right)
            result.append(root.data)
        return result
    

    #preorder traversal root-->left-->right
    def preorder(self, root):
        result = []
        if root:
            result.append(root.data)
            result = result + self.inorder(root.left)
            result =  result + self.inorder(root.right)
            
        return result



root = Node(8)
root.Insert(6)
root.Insert(5)
root.Insert(7)
root.Insert(4)
root.Insert(9)
root.Insert(11)
root.Insert(13)
root.Insert(10)
root.Insert(1)

#root.display()

print( root.inorder(root))
print( root.postorder(root))
print( root.preorder(root))
print(root.search(8))
