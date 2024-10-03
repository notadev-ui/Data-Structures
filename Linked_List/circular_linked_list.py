# Defining a class for the node
class node:
    def __init__(self, data):
        # data will store the actual value of the node
        self.data = data
        # next will point to the next node in the linked list, initially set to None
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

    #deletion at specified position
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
            

    #method of searching elements 
    def search(self):
        x = int(input("Enter element to be search in ccl: "))
        temp = self.head
    
        count = 0
        flag = 0
        while temp != self.tail:
            if x == temp.data:
                flag = 1
                break
            temp = temp.next
            count += 1
            if temp == self.head:  # Break if we have looped back to the head
              break
    
        if flag == 1:
                print(x,"found", count+1)
        else:
                print(x,"not found")


    
    # Method to display the elements of the linked list
    def display(self):
        if self.head is None: 
            print("Linked list is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                if (temp.next == self.head):
                    break
                temp = temp.next
            


L = CircularLinkedList()
"""
# Creating nodes with data
n = node(10)   # First node with data 10
L.head = n     # Assigning the first node as the head of the linked list
L.tail = n
L.tail.next = L.head

n1 = node(20)  # Second node with data 20
L.tail.next = n1    # Linking first node to second node
L.tail = n1
L.tail.next = L.head

n2 = node(30)  # Third node with data 30
L.tail.next = n2   # Linking second node to third node
L.tail = n2
L.tail.next = L.head

n3 = node(40)  # Fourth node with data 40
n2.next = n3   # Linking third node to fourth node

n4 = node(50)  # Fifth node with data 50
n3.next = n4   # Linking fourth node to fifth node
n4.next = n"""

L.display()
L.insert(10)
L.insert(20)
L.insert(30)
L.insert(40)
L.insert(50)
L.insert(60)
L.insert(70)
L.insert(80)
L.display()
"""
print("")
L.insert_at_beginning(5)
L.display()

print("next")
L.insert_at_end(90)
L.display()

L.insert_at_anyPos(7,25)
print("insert at any pos")
L.display()

print("delete the first element")
L.del_at_beginning()
L.display()

print("delete the last element")
L.del_at_end()
L.display()

print("delete any element")
L.del_at_anyPos(7)
L.display()
"""
L.search()
