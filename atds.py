#!/usr/bin/env python3

"""
atds.py

Write a Python class Stack that implements this abstract data type. The Stack class will include:
a. a constructor which creates an empty stack
b. the .push(item) method to push an item onto the stack
c. the .pop() method to remove an item from the stack, and return that removed item as a result
d. the .peek() method which returns the value of the top item in the stack
e. the .size() method which returns the number of items in the stack
f. the .isEmpty() method which returns True or False, depending on the state of the stack
"""

__author__ = "Kaylin Yagura"
__version__ =  "2/10/23"


class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False


"""
A "queue," like a "stack," is an ordered collection of items. Items can be "queued" onto the 
end of the queue, in order, with items queued later being placed behind items that have arrived earlier. 
When items are removed from the queue they are "dequeued" from the front in a "first come, 
first served" fashion. The item at the front of the queue can be "peeked" at (
identified without removing it from the queue), and the "size" of the queue can be 
identified at any time. Also, the queue can be identified as being "empty" (a size of 0).

Write a Python class Queue that implements this abstract data type using a list. The Queue class will include:

a constructor which creates an empty queue
the enqueue(item) method to place an item onto the back of the queue
the dequeue() method to remove an item from the front of the queue, and return that removed item as a result
the peek() method which returns the value of the item at the front of the queue without removing it
the size() method which returns the number of items in the queue
the isEmpty() method which returns True or False, depending on the state of the queue
"""

class Queue(object):
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    """def enqueue(self, item):
        self.queue.insert(0,item)
    """

    def dequeue(self):
        return self.queue.pop(0)

    """def dequeue(self):
        return self.queue.pop()
        """

    def peek(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def print_queue(self):
        l = ""
        for e in self.queue:
            l += e
            l += " "
        return l

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False



"""
The Deque class is a "double-ended Queue," and not to be confused with the word "dequeue." 
The double-ended queue allows one to add values to the front or rear of the queue, 
and allows for values to be removed from the front or rear of the queue.

For the Deque class write:

the Deque constructor
addFront(item)
addRear(item)
removeFront()
removeRear()
size()
isEmpty()

"""

class Deque(object):
    def __init__(self):
        self.deque = []
    
    def add_front(self, item):
        self.deque.insert(0, item)
    
    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        return self.deque.pop(0)

    def remove_rear(self):
        return self.deque.pop()
    
    def size(self):
        return len(self.deque)
    
    def print_deque(self):
        l = ""
        for e in self.deque:
            l += e
            l += " "
        return l
    
    def compare(self, object):
        if self.deque == object.deque:
            return True
        else:
            return False


    def is_empty(self):
        if len(self.deque) == 0:
            return True
        return False



