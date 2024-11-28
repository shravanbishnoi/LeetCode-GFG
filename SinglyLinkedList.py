"""
This script contains implementation of SLL
"""

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    class Node:
        def __init__(self, value, nxt=None):
            self.data = value
            self.next = nxt

    def insert(self, data, next=None):
        new_node = self.Node(data, next)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return new_node

    def delete(self, data):
        if self.size == 0:
            return "List is empty"

        current = self.head
        prev = None

        while current is not None:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                    if self.size == 1:
                        self.tail = None
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                self.size -= 1
                return current
            prev = current
            current = current.next

        return "Node with the given value not found"

    def is_empty(self):
        return self.size == 0

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def deleteMiddle(self):
        if self.is_empty():
            return "List is empty"
        elif self.size < 3  :
            node = self.head.data
            self.head = self.head.next
            return self.head.data
        slow = self.head
        fast = self.head.next.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        node = slow.next.data
        slow.next = slow.next.next
        return node
    
if __name__=='__main__':
    values = [2, 1, 4, -1, 5, 10, 11, 5, 3]
    SLL = SinglyLinkedList()
    for value in values:
        SLL.insert(value)
    SLL.display()
    print("Deleted middle node value: ", SLL.deleteMiddle())
    SLL.display()


