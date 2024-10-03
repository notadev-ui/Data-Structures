
import array as arr

# Create an array 
my_array = arr.array('i', [1, 2, 3, 4, 5, 6])

# (i) Add a new element to an array
my_array.append(7)
print(my_array)

# (ii) Add four elements to an array
my_array.extend([8, 9, 10, 11])
print(my_array)

# (iii) Add an element at the fourth position
my_array.insert(3, 100)
print(my_array)

# (iv) Delete the seventh element from the left of an array
del my_array[6]
print(my_array)

# (v) Remove the last element and return it
last_element = my_array.pop()
print(my_array)

# (vi) Create two arrays having three elements each and merge all three arrays
array1 = arr.array('i', [12, 13, 14])
array2 = arr.array('i', [15, 16, 17])
merged_array = my_array + array1 + array2

# (vii) Display the array formed in question (vi)
print("Merged array:", merged_array)

# (viii) Determine the length of the new array formed
length_of_merged_array = len(merged_array)
print("Length of merged array:", length_of_merged_array)

# (ix) Print the ninth element of the new array
if len(merged_array) >= 9:
    print("Ninth element of merged array:", merged_array[8])
else:
    print("The array has less than 9 elements")
