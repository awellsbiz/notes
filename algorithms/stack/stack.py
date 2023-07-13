"""
A stack is an Abstract Data Type (ADT), that is popularly used in most programming languages. It is named stack because it has the similar operations as the real-world stacks, for example – a pack of cards or a pile of plates, etc.

The stack follows the LIFO (Last in - First out) structure where the last element inserted would be the first element deleted.

A Stack ADT allows all data operations at one end only. At any given time, we can only access the top element of a stack.

A stack can be implemented by means of Array, Structure, Pointer, and Linked List. Stack can either be a fixed size one or it may have a sense of dynamic resizing

The most fundamental operations in the stack ADT include: `push()`, `pop()`, `peek()`, `isFull()`, `isEmpty()`.
"""

# PUSH
"""
Algorithm
1 Checks if the stack is full.
2 If the stack is full, produces an error and exit.
3 If the stack is not full, increments top to point next empty space.
4 Adds data element to the stack location, where top is pointing.
5 Returns success.
"""

class Stack:
   def __init__(self):
      self.stack = []
   def push(self, data):
      if data not in self.stack:
         self.stack.append(data)
         return True
      else:
         return False

stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk)
# output: [1, 2, 3]

# POP
"""
Algorithm
1 − Checks if the stack is full.
2 − If the stack is full, produces an error and exit.
3 − If the stack is not full, increments top to point next empty space.
4 − Adds data element to the stack location, where top is pointing.
5 − Returns success.
"""

class Stack:
   def __init__(self):
      self.stack = []
   def push(self, data):
      if data not in self.stack:
         self.stack.append(data)
         return True
      else:
         return False

stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk)
# output: [1, 2, 3]

# PEEK
"""
Algorithm
1. START
2. return the element at the top of the stack
3. END
"""

class Stack:
    def __init__(self):
      self.stack = []
    def push(self, data):
        if data not in self.stack:
         self.stack.append(data)
         return True
        else:
         return False
    def pop(self):
        if len(self.stack) <= 0:
            print("No element in the Stack")
        else:
            return self.stack.pop()
    def peek(self):
      return self.stack[-1]

stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk)
# output: [1, 2, 3]
print("topmost element: ",stk.peek())
#topmost element:  3