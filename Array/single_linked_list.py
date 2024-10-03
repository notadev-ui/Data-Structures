# Defining a class for the node
class node:
    def __init__(self, data):
        # data will store the actual value of the node
        self.data = data
        # next will point to the next node in the linked list, initially set to None
        self.next = None

# Defining a class for the singly linked list
class SingleLinkedList:
    def __init__(self):
        # head will store the first node of the linked list, initially set to None (empty list)
        self.head = None

    # Method of insertion at begining
    def insert_at_beginning(self,data):
        nb = node(data)
        nb.next = self.head
        self.head = nb

    #method of deletion at beginning
    def del_at_beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None


    #method of insertion at end
    def insert_at_end(self,data):
        ne = node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    #deletion at end
    def del_at_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None   


    #Method of insertion at specified position
    def insert_at_anyPos(self,pos,data):
        np = node(data)
        temp = self.head
        for i in range(1,pos - 1):
            temp = temp.next 
        np.data = data
        np.next = temp.next
        temp.next =np
        
    #deletion at specified position
    def del_at_anyPos(self,pos):
        temp = self.head.next
        prev = self.head
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None




    # Method to display the elements of the linked list
    def display(self):
        if self.head is None:  # Checking if the linked list is empty
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

# Creating an empty singly linked list
L = SingleLinkedList()

# Creating nodes with data
n = node(10)   # First node with data 10
L.head = n     # Assigning the first node as the head of the linked list

n1 = node(20)  # Second node with data 20
L.head.next = n1    # Linking first node to second node

n2 = node(30)  # Third node with data 30
n1.next = n2   # Linking second node to third node

n3 = node(40)  # Fourth node with data 40
n2.next = n3   # Linking third node to fourth node

n4 = node(50)  # Fifth node with data 50
n3.next = n4   # Linking fourth node to fifth node

# Display the linked list elements
L.display()

print("")
L.insert_at_beginning(5)
L.display()

print("next")
L.insert_at_end(60)
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