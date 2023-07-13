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