"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# from stack import Stack  # pylint: disable=import-error
# from singly_linked_list import LinkedList  # pylint: disable=import-error
# import sys
# sys.path.extend(['singly_linked_list', 'stack'])

# 1. Queue (using an array)
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     # len performance: O(1)
#     def __len__(self):
#         return self.size

#     # enqueue performance: O(1)
#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     # dequeue performance: O(n)
#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop(0)


# 2. Queue (using a linked list)
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def isEmpty(self):
        return self.size == 0

    # len performance: O(1)
    def __len__(self):
        return self.size

    # enqueue performance: O(1)
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    # dequeue performance: O(1)
    def dequeue(self):
        print(self.storage)
        if self.isEmpty():
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
    
    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def add_to_tail(self, value):
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None

        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None

            return head.get_value()

        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

            value = self.tail.get_value()
            self.tail = current
            return value

    def contains_self(self, value):
        if not self.head:
            return False

        current = self.head
        while current:
            if current.get_value() == value:
                return True
                current = current.get_next()
                return False

    def get_max(self):
        max_value = self.head.get_value()
        current = self.head.get_next()
        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
                current = current.get_next()
                return max_value

myQueue = Queue()
myQueue.enqueue(17)
myQueue.enqueue(20)
print(myQueue.dequeue())
