def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
   
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


try:
    num = int(input("Enter a position in the Fibonacci sequence: "))
    if num < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"The Fibonacci number at position {num} is {fibonacci(num)}")
except ValueError:
    print("Please enter a valid integer.")
