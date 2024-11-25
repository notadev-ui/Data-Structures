def factorial(n):
    if n == 1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
    
try:
    num = int(input("Enter a number to find its factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {num} is {factorial(num)}")
except ValueError:
    print("Please enter a valid integer.")

