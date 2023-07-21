"""
Two pointers algorithm is a technique that uses two pointers to solve a problem.

The two pointers can be in the same direction or in the opposite direction.

For example, you can use two pointers to find the sum of two numbers in a sorted array.

The two pointers algorithm can be used to solve other problems such as finding the intersection of two arrays, removing duplicates from a sorted array, or solving a linked list cycle problem.

The Two pointer approach has 3 steps:

    1. Initialize two pointers: pointers can start at any place depending on what we are trying to achieve. 
        - For example, if we are trying to find the sum of two numbers in a sorted array, we can initialize one pointer at the beginning and the other pointer at the end. If we are trying to find the intersection of two arrays, we can initialize both pointers at the beginning of the arrays.

    2. Move the pointers: we move the pointers depending on the problem we are trying to solve. They can move in the same direction or in the opposite direction. Also, we can move them at different speeds (slow and fast pointers).
     
        - For example, if we are trying to find the sum of two numbers in a sorted array, we move the pointers towards the middle of the array. If we are trying to find the intersection of two arrays, we move the pointers depending on the values of the elements at the pointers.
    
    3. Terminate: we terminate the algorithm when we find the solution to the problem we are trying to solve.
"""

# Reverse a list using two pointers

# input: [1, 2, 3, 4, 5]
# output: [5, 4, 3, 2, 1]

def reverse_list(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -+ 1

    return arr

print(reverse_list([1, 2, 3, 4, 5]))

# Giiven an integer array sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# input: [-4, -1, 0, 3, 10]
# output: [0, 1, 9, 16, 100]

def sorted_squares(nums):
    #square each number
    squares_nums = [num**2 for num in nums]
    #sort the numbers
    squares_nums.sort()
    return squares_nums

input = [-4, -1, 0, 3, 10]
output = sorted_squares(input)
print(output)
   
