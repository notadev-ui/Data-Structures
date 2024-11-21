# Defining a class for the node
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        # head will store the first node of the linked list, initially set to None (empty list)
        self.head = None
        self.tail = None
    
    def insert(self, data):
        new_node = node(data)  # Create a new node with the given data
        
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            self.tail = new_node  # Set the new node as the tail
            new_node.next = self.head  # The new node points to itself, making the list circular
        else:
            self.tail.next = new_node  # The current tail points to the new node
            self.tail = new_node  # The new node becomes the new tail
            self.tail.next = self.head  # The new tail points to the head, maintaining circularity
    
    # Method of insertion at begining
    def insert_at_beginning(self,data):
        nb = node(data)
        nb.next = self.head
        self.tail.next = nb
        self.head = nb

    #method of deletion at beginning
    def del_at_beginning(self):
        if self.head is None:
            print("cell is empty")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.tail.next = self.head

        
    #method of insertion at end
    def insert_at_end(self,data):
        ne = node(data)
        temp = self.head
        while temp.next != self.head :
            temp = temp.next
        temp.next = ne
        tail = ne
        tail.next = self.head
    
    #deletion at end
    def del_at_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next != self.head:
            temp = temp.next
            prev = prev.next
        prev.next = None   
        prev = prev.next

    #Method of insertion at specified position
    def insert_at_anyPos(self,pos,data):
        np = node(data)
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next 
        np.data = data
        np.next = temp.next
        temp.next = np

    def del_at_anyPos(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None
        if temp.next == self.tail:
            self.tail = self.head
            
    def display(self):
        if self.head is None: 
            print("Linked list is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ->")
                if (temp.next == self.head):
                    break
                temp = temp.next
            print("back to head")
            


L = CircularLinkedList()

# Creating nodes with data
n = node(10)   # First node with data 10
L.head = n     # Assigning the first node as the head of the linked list
L.tail = n
L.tail.next = L.head

n1 = node(20)  # Second node with data 20
L.tail.next = n1    # Linking first node to second node
L.tail = n1
L.tail.next = L.head

L.display()
L.insert(30)
L.insert(40)
L.insert(50)
L.display()

print("insert at beginning")
L.insert_at_beginning(5)
L.display()

print("insert at end")
L.insert_at_end(60)
L.display()

L.insert_at_anyPos(4,25)
print("insert at any pos")
L.display()

print("delete the first element")
L.del_at_beginning()
L.display()

print("delete the last element")
L.del_at_end()
L.display()

print("delete any element")
L.del_at_anyPos(4)
L.display()

