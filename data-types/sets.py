"""
A set is an unordered collection with no duplicate elements. Sets are iterable and mutable. Order of elements in a set is undefined and is unchangeable. Type of elements in a set need not be the same, various mixed-up data type values can also be passed to the set.

The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

The disadvantages of sets are that they are unordered, have limited funtionality compared to lists (they do not support methods like append or pop), sets can consume more memory than lists (especially for small datasets) because each element in a set requires additional memory to store a hash value, and sets are less commonly used so there may be fewer resources or libraries available for working with them. 

Note: to create an empty set you have to use set()
"""
andrew = set("andrew")
print(andrew)
# output: {'d', 'r', 'n', 'a', 'w', 'e'}

mixed = set([98, "Earth", True, "Hello", 39])
print(mixed)
# output: {True, 98, 39, 'Hello', 'Earth'}


### METHODS

# ADD
"""
Adds an element to a set
"""
andrew = set("andrew")
andrew.add('h')
print(andrew)
# output: {'e', 'r', 'd', 'h', 'a', 'w', 'n'}

# REMOVE
"""
Removes an element from a set. If the element is not present in the set, raise a KeyError
"""
andrew = set("andrew")
andrew.remove('w')
print(andrew)
# output: {'a', 'd', 'n', 'e', 'r'}

# CLEAR
"""
Removes all elements from a set
"""
murphy = set("murphy")
murphy.clear()
print(murphy)
# output: set()

# COPY
"""
Returns a shallow copy of a set
"""
snack = set("cookies")
cookies = snack.copy()
print(cookies)
# output: {'i', 'e', 's', 'k', 'o', 'c'}

# POP
"""
Removes and returns an arbitrary set element. Raise KeyError if the set is empty
"""
memory = set("memory")
memory.pop()
print(memory)
# output: {'m', 'y', 'e', 'r'}

# UPDATE
"""
Updates a set with the union of itself and others
"""
murphy = set("murphy")
andrew = set("andrew")
kate = set("kate")
murphy.update(andrew, kate)
print(murphy)
# output: {'t', 'h', 'k', 'm', 'p', 'e', 'y', 'n', 'u', 'd', 'r', 'a', 'w'}

# UNION
"""
Returns the union of sets in a new set
"""
a = set("abc")
b = set("def")
print(a.union(b))
# output: {'b', 'a', 'd', 'e', 'c', 'f'}

# DIFFERENCE
"""
Returns the difference of two or more sets as a new set
"""
a = set("abcdefg")
b = set("def")
c = set("cg")
print(a.difference(b, c))
# output: {'b', 'a'}

# DIFFERENCE_UPDATE
"""
Removes all elements of another set from this set
"""
a = set({'apple', 'orange', 'berry'})
b = set({"apple"})
c =set({"orange"})
a.difference_update(b, c)
print(a)
# output: {'berry'}

# DISCARD
"""
Removes an element from set if it is a member. (Do nothing if the element is not in set)
"""
a = set({'apple', 'orange', 'berry'})
a.discard('orange')
print(a)

# INTERSECTION
"""
Returns the intersection of two sets as a new set
"""
a = set({'apple', 'orange', 'berry'})
b = set({'apple', 'berry', 'pie'})
print(a.intersection(b))
# output: {'apple', 'berry'}

# INTERSECTION_UPDATE
"""
Updates the set with the intersection of itself and another
"""
a = set({'apple', 'orange', 'berry'})
b = set({'apple', 'berry', 'pie'})
a.intersection_update(b)
print("Intersection update")
print(a)
# output: {'berry', 'apple'}

# ISDISJOINT
"""
Returns True if two sets have a null intersection
"""
a = set({'apple', 'orange', 'berry'})
b = set({'apple', 'berry', 'pie'})
c = set({'ice cream'})
print(a.isdisjoint(b))
# output: False
print(a.isdisjoint(c))
# output: True

# ISSUBSET
"""
Returns True if another set contains this set
"""
a = set({'apple', 'berry'})
b = set({'apple', 'berry', 'pie'})
print(a.issubset(b))
# output: True
print(b.issubset(a))
# output: False
