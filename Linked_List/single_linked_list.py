# Defining a class for the node
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        nb = node(data)
        nb.next = self.head
        self.head = nb

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
        for i in range(pos - 1):
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
                print(temp.data,end=" ->")
                # Move to the next node
                temp = temp.next
            print("Null")

# Creating an empty singly linked list
L = SingleLinkedList()

# Creating nodes with data
n = node(10)   
L.head = n     # 

n1 = node(20)  
L.head.next = n1    

L.display()

print("\n")
print("Inserting nodes at different position")
L.insert_at_beginning(5)
L.display()

L.insert_at_end(60)
L.display()

L.insert_at_anyPos(3,25)
L.display()


print("\n")
print("Deleting nodes at different position")
L.del_at_beginning()
L.display()

L.del_at_end()
L.display()

L.del_at_anyPos(3)
L.display()