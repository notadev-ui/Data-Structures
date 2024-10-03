class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class double_linked_list():
    def __init__(self) :
        self.head = None
    
    def insert_at_beginning(self,data):
        n = node(data)
        temp = self.head
        temp.prev = n
        n.next = temp
        self.head = n

     #method of deletion at beginning
    def del_at_beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None

     #deletion at end
    def del_at_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None 
        temp.next = None  



    def insert_at_end(self,data):
        n = node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = n
        temp.prev = temp

    
    def insert_at_anyPos(self,pos,data):
        n = node(data)
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next 
        n.data = data
        n.prev = temp
        n.next = temp.next
        temp.next =n
        temp.next.prev = n
    
     #deletion at specified position
    def del_at_anyPos(self,pos):
        temp = self.head.next
        prev = self.head
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next.prev = prev
        temp.next = None
        temp.prev = None



    def display(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            # Start from the head node
            temp = self.head
            # Traverse the linked list until the last node
            while temp:
                # Print the data of the current node
                print(temp.data)
                # Move to the next node
                temp = temp.next

L = double_linked_list()
n1 = node(10)
L.head = n1

n2 = node(20)
n2.prev = n1
n1.next = n2

n3 = node(30)
n3.prev = n2
n2.next = n3

n4 = node(40)
n4.prev = n3
n3.next = n4

L.display()
print("")
L.insert_at_beginning(5)
L.display()

print("next")
L.insert_at_end(50)
L.display()

L.insert_at_anyPos(3,25)
print("insert at any pos")
L.display()
        
print("delete the first element")
L.del_at_beginning()
L.display()       


print("delete the last element")
L.del_at_end()
L.display()

print("delete any element")
L.del_at_anyPos(3)
L.display()