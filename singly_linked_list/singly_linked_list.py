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

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
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
    
    removed_value = self.head.get_value()
    self.head = self.head.next
    if not self.head:
        self.tail = None
    return removed_value

def remove_tail(self):
    if not self.tail:
        return None
