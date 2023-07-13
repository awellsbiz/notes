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

# CLEAR
"""
list.clear() - removes all items from list
"""
nums_list = [3, 6, 9, 12, 15, 18]
nums_list.clear()
print(nums_list)
# output: []

# REMOVE
"""
list.remove(x) - removes the first item from the list whose value is equal to `x`. It throws a `ValueError` if there is no such item
"""
nums_list = [3, 6, 9, 12, 15, 18]
nums_list.remove(15)
print(nums_list)
# output: [3, 6, 9, 12, 18]

# COUNT
"""
list.count(x) - returns the amount of instances of a given value x.
"""
nums_list = [3, 6, 9, 12, 15, 18, 3, 6, 9, 12, 15, 18, 3, 6, 9]
nums_list.count(15)
# output: 2
nums_list.count(9)
# output: 3

# SORT
"""
list.sort() - sorts the items of the list in place. sort(key=..., reverse=...) arguments can be used for sort customizations
"""
nums_list = [15, 9, 6, 3, 12, 18]
nums_list.sort()
print(nums_list)
# output: [3, 6, 9, 12, 18]

# sorting using reverse=True (false by default)
nums_list = [15, 9, 6, 3, 12, 18]
nums_list.sort(reverse=True)
print(nums_list)
#output: [18, 15, 12, 9, 6, 3]

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25},
    {'Name': 'Sharon Lin', 'age': 30},
    {'Name': 'John Hopkins', 'age': 18},
    {'Name': 'Mikhail Tal', 'age': 40},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')

def get_age(employee):
    return employee.get('age')

# sort by name
[{'Name': 'Alan Turing', 'age': 25}, {'Name': 'John Hopkins', 'age': 18}, {'Name': 'Mikhail Tal', 'age': 40}, {'Name': 'Sharon Lin', 'age': 30}][{'Name': 'Alan Turing', 'age': 25}, {'Name': 'John Hopkins', 'age': 18}, {'Name': 'Mikhail Tal', 'age': 40}, {'Name': 'Sharon Lin', 'age': 30}]
# output: [{'Name': 'Alan Turing', 'age': 25}, {'Name': 'John Hopkins', 'age': 18}, {'Name': 'Mikhail Tal', 'age': 40}, {'Name': 'Sharon Lin', 'age': 30}]

# sort by Age
employees.sort(key=get_age)
print(employees, end='\n\n')
# output: [{'Name': 'John Hopkins', 'age': 18}, {'Name': 'Alan Turing', 'age': 25}, {'Name': 'Sharon Lin', 'age': 30}, {'Name': 'Mikhail Tal', 'age': 40}]

# REVERSE
"""
list.reverse() - reverse the elements of the list in place
"""
nums_list = [3, 6, 9, 12, 15, 18]
nums_list.reverse()
print(nums_list)
# output: [18, 15, 12, 9, 6, 3]

# COPY
"""
list.copy() or list[:] - returns a shallow copy of the list
"""
nums_list = [3, 6, 9, 12, 15, 18]
nums = nums_list.copy()
nums_copy = nums_list[:]
print(nums)
# output: [3, 6, 9, 12, 15, 18]
print(nums_copy)
# output: [3, 6, 9, 12, 15, 18]