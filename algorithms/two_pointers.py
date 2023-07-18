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
