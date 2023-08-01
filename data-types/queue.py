"""
Queue is a linear data structure that follows the FIFO (First In First Out) principle. This approach is quite similar to real-life queues like a queue of customers waiting at a ticket counter, queue of people waiting at the bus stand, etc.

The opposite of Stack

Some advantages of using a queue are:
    - It is easy to implement as it is based on the FIFO principle.
    - Insertion and deletion are allowed at different ends.
    - Can add new items at the end of the queue and remove items from the front of the queue.

Some disadvantages of using a queue are:
    - It is not easy to delete an element from the middle of the queue.
    - Difficult to create and maintain 
    - Its a non linear data structure that takes alot of memory.

The queue data structure is used when we want to organize the group of objects in a particular order. Think a Printer Queue, where the first document in the queue is the first document printed, or a call center queue, where the first call in the queue is the first call answered.

"""

# Simple Queue Data Structure:

class demo_queue:
    def __init__(self):
        self.queue = []

    # add an element to the queue
    def enqueue(self, item):
         if item not in self.queue:
             self.queue.insert(0,item)
             return True
         return False
    # remove an element from the queue
    def dequeue(self):
            if len(self.queue)>0:
                return self.queue.pop()
            return ("Queue Empty!")
    def size(self):
        return len(self.queue)
    
Queue = demo_queue() 
Queue.enqueue("Mon")
Queue.enqueue("Tue")
Queue.enqueue("Wed")
print(Queue.size())
Queue.dequeue()
print(Queue.size())
print(Queue.queue)
    
    

    