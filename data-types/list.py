"""
Lists are a collection of arbitrary objects, just like arrays in other programming languages. 

Lists are ordered. 

Lists are accessed using the idnex - which starts at 0.

Lists are mutable and dynamic which means they can be modified after their creation.

Example:
    list = ['p', 'y', 't', 'h', '0', 'N']
    list[3] = 'h'
"""

### Methods

# INDEX
"""
list.index(x) - return zero-based index in the list of the first item whose value is equal to x. Also can use parameters to start the search further in the list list.index(element, index start, index end)
"""
nums_list = [3, 6, 9, 6, 15, 9, 6, 3]
nums_list.index(6)
# output: 1
nums_list.index(6, 5)
# output: 6
nums_list.index(6, 2, 5)
# output: 3

# INSERT
"""
list.insert(index, element) - inserts a single element anywhere in the list
"""
nums_list = [3, 6, 9, 15]
nums_list.insert(3, 12)
print(nums_list)
# output: [3, 6, 9, 12, 15]

# APPEND
"""
list.append(item) - always adds items (strings, numbers, lists) at the end of the list
"""
nums_list = [3, 6, 9, 12, 15]
nums_list.append(18)
print(nums_list)
# output: [3, 6, 9, 12, 15, 18]

# EXTEND
"""
list.extend(item) - adds iterable items (lists, tuples, strings) to the end of the list
"""
nums_list = [3, 6, 9, 12, 15, 18]
nums_list_extended = [21, 24, 27, 30]
nums_list.extend(nums_list_extended)
print(nums_list)
# output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# POP
"""
list.pop(index) - deletes the last item of the list. If there is no item in the list, an IndexError will be thrown
"""
nums_list = [3, 6, 9, 12, 15, 18]
nums_list.pop()
print(nums_list)
# output: [3, 6, 9, 12, 15]
nums_list = [3, 6, 9, 12, 15]
nums_list.pop(2)
print(nums_list)
nums_list = [3, 6, 12, 15]