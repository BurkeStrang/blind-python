# Template for linked list node class

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # __eq__ will be used for testing
    # to compare two LinkedListNode type objects.
    def __eq__(self, other):
        if not isinstance(other, LinkedListNode):
            return False
        return self.data == other.data and self.next == other.next
