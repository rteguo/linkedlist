"""
Linked list with Node and LinkedList classes

"""
class Node:
    """Node is a linked list"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"<Node Object. Data : {self}; Next : {self.next} >"
    

class LinkedList:
    """Linked list using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"<Linked list. Head : {self.head}; Tail : {self.tail}>"
    
    def append(self, data):
        """Append Node with data to end of linked list."""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        
        if self.tail:
            self.tail.next = new_node

        self.tail = new_node



