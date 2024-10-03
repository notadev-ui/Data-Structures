import array as arr

# Function to create an array with user-defined length and elements
def create_user_array():
    # Asking the user to define the length 
    n = int(input("Enter the length of the array: "))

    # Creating an empty array of integers
    user_array = arr.array('i', [])

    # Asking the user to input the elements
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        user_array.append(element)

    # Displaying the created array
    print("Created array:", user_array)

# Call the function to create and display the user-defined array
create_user_array()
