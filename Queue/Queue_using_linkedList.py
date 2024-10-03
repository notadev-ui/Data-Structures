class node:
    def __init__(self,x) :
        self.data = x
        self.next = None

class Queue:
    def __init__(self) :
        self.front = None
        self.rear = None

    def enqueue(self):
       x = int(input("Enter element to be inserted into queue: "))
       new = node(x)
       if self.front == None:
           self.front = new
           self.rear = new
       else:
           self.rear.next = new
           self.rear =new


    def dequeue(self):
        if Queue is None:
            print("Queue is empty")
        else:
            temp = self.front
            print("popped element is: ",self.front.data)
            self.front = temp.next
            temp = None
    
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("element of the Queue are:")
            temp = self.front
            while temp:
                print(temp.data)
                temp = temp.next
            print("front of the Queue is:", self.front.data)
            print("Rear of queue is:",self.rear.data)



Queue = Queue()    

while True:
    print("Enter the option from below\n1-Enqueue operation\n2-dequeue Operatuon\n3-Display\n4-Enter any key to exit")
    option = input()
    if option == "1":
        print("Enqueue Operation")
        Queue.enqueue()
    elif option == "2":
        print("Dequeue Operation")
        Queue.dequeue()
    elif option == "3":
        print("Display Operation")
        Queue.display()
    else:
        print("Exit from the program")
        break


            