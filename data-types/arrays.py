"""
A List in Python is a collection of items which can contain elements of multiple data types. They are ordered, mutable, do not need to be unique (can be duplicated), and can be of different data types. List are more commonly used than arrays.


An Array is a data structure for storing more than one data item that has a similar data type. Like list they are ordered, mutable, and allow duplicate elements.

In Python, arrays are different from lists; lists can have array items of data types, whereas arrays can only have items of the same data type. Usually, integers, floats, and characters are stored in arrays.

Arrays are great for numerical operations; lists cannot directly handle math operations. For example, you can divide each element of an array by the same number with just one line of code. If you try the same with a list, you'll get an error.

Python has a separate module for handling arrays called array, which you need to import before you start working on them.
    use import array or NumPy package to create arrays in Python. ( they have different syntax )

    You delacre an array in python while initializing it like so:
        array_name = array.array(typecode, [Initializers]) (check the docs for more info on typecode)


"""

# Array Opperations in Python

import array

# creating an array
arr = array.array('i', [1, 2, 3, 4, 5, 6])

# printing original array
print("The new created array is : ", arr)

# Output: The new created array is :  array('i', [1, 2, 3, 4, 5, 6])

# You can access an array element by referring to its index number.

print(arr[2])

# Insert: array.insert(index, value)

arr.insert(3, 10)

print(arr)
# Output: array('i', [1, 2, 3, 10, 4, 5, 6])

# Remove: array.remove(value)

arr.remove(10)

print(arr)
# Output: array('i', [1, 2, 3, 4, 5, 6])

# Search: array.index(value)

print(arr.index(5))
# Output: 4

# Update: new[index] = value

arr[2] = 100
print(arr)
# Output: array('i', [1, 2, 100, 4, 5, 6])

# Append: array.append(value)
# Pop: array.pop(index)


"""
To perform Math operations alot faster than using list- use the NumPy library. Its often used for data science and machine learning.
"""


