class node:
    def __init__(self,x) :
        self.data = x
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        data = int(input("Enter the element push into stack:"))
        new = node(data)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
           new.next = self.top
           self.top = new
          

    def pop(self):
        if Stack is None:
            print("Stack is empty")
        
        else:
            temp = self.top
            print("popped element is :",self.top.data)
            self.top = temp.next
            temp = None

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("element of the stack are:")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print("Top of the stack is")


stack = Stack()    

while True:
    print("Enter the option from below\n1-PUSH operation\n2-POP Operatuon\n3-Display\n4-Enter any key to exit")
    option = input()
    if option == "1":
        print("Push Operation")
        stack.push()
    elif option == "2":
        print("POP Operation")
        stack.pop()
    elif option == "3":
        print("Display Operation")
        stack.display()
    else:
        print("Exit from the program")
        break


            