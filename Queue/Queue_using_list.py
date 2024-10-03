
def enqueue():
    n = int(input("Enter the element push into queue:"))
    queue.append(n)
    
def dequeue():
    if len(queue) == 0 :
       print("queue is empty")
    else:
        print(queue[0],"is deleted from queue")
        del queue[0] #pop[0]

def display():
    if len(queue) == 0:
        print('queue is empty')
    else:
        for i in queue:
            print(i)
        
        print("\nFront of the queue is", queue[0])
        print("Rear of the queue is", queue[-1])
        print()




queue = list()

while True:
    print("Enter the option from below\n1-Enqueue operation\n2-dequeue Operatuon\n3-Display\n4-Enter any key to exit")
    option = input() 
    if option == "1":
        print("Enqueue Operation")
        enqueue()
    elif option == "2":
        print("Dequeue Operation")
        dequeue()
    elif option == "3":
        print("Display Operation")
        display()
    else:
        print("Exit from the program")
        break

