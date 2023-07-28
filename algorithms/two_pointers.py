"""
Two pointers is an effective technique that is typically used for searching pairs in a sorted array.

A pointer is a reference to an object. 

When might we use it? 
Problems that involve collections such as arrays or lists, when we have to analyze each element of the collection compared to its other elements. 
"""

# REVERSE ARRAY EXAMPLE
def reverseArray(array):
    start, end = 0, len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

array = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
reverseArray(array)
print(array)
# output: [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]


# TWO SUM EXAMPLE
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
def twoSum(nums_list, target):
    # sort the nums list
    nums = nums_list.copy()
    nums.sort()
    # initialize pointers
    left = 0
    right = len(nums) - 1
    # pointer movement, in this case, will bring the pointers together, but they won't ever equal each other.
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            values = [nums[left], nums[right]]
            # note: because we sorted the list, these indexes of correct values don't match the original list
            break
        elif sum < target:
        # if the sum is less than the target, we need to move our lower value (left pointer) to the right
            left += 1
        else:
        # if the sum is too great, we need to move our higher value (right pointer) to the left
            right -= 1
    # now we need to compare the original indexes to the correct values
    output = []
    i = 0
    while len(output) < 2:
        if nums_list[i] == values[0]:
            output.append(i)
            i += 1
        elif nums_list[i] == values[1]:
            output.append(i)
            i += 1
        else:
            i += 1
    return output

nums_list = [4, 3, 6, 1, 2]
target = 6
print(twoSum(nums_list, target))

# Given an integer array sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums):
    n = len(nums)
    start, end = 0, n-1
    res = [0]*n
    i = n-1
    while end > -1 and i > -1:
        if abs(nums[start]) > abs(nums[end]):
            res[i] = nums[start] * nums[start]
            start += 1
        else:
            res[i] = nums[end] * nums[end]
            end -= 1
        i -= 1
    return res


print(sortedSquares([-4,-3,0,2,6,9]))
# output: [0, 4, 9, 16, 36, 81]




# Given an integer array sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

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
   
