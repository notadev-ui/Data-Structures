def push():
    n = int(input("Enter the element push into stack:"))
    if len(stack) == 0 :
        stack.append(n)
    else:
        stack.insert(0,n)
    print(n,"is inserted into stack ")

def pop():
    if len(stack) == 0 :
       print("Stack is empty")
    else:
        print(stack[0],"is deleted from stack")
        del stack[0] #pop[0]

def display():
    if len(stack) == 0:
        print('Stack is empty')
    else:
        for i in range:
            print(i,)
    print("Top of the stack is", stack[0])

        


stack = list()      

while True:
    print("Enter the option from below\n1-PUSH operation\n2-POP Operatuon\n3-Display\n4-Enter any key to exit")
    option = input()  
    if option == "1":
        print("Push Operation")
        push()
    elif option == "2":
        print("POP Operation")
        pop()
    elif option == "3":
        print("Display Operation")
        display()
    else:
        print("Exit from the program")
        break
