"""
Write code to remove duplicates from an unsorted linked list.
"""

from SinglyLinkedList import SinglyLinkedList

def removeDuplicates(sll):
    if sll.is_empty():
        return "Singly linked list is empty"

    elements = set()
    current = sll.head
    previous = None

    while current:
        if current.data in elements:
            previous.next = current.next
        else:
            elements.add(current.data)
            previous = current
        current = current.next

    return sll

values = [2, 1, 3, 3, 2, 1, 1, 2]
SLL = SinglyLinkedList()
for value in values:
    SLL.insert(value)
SLL.display()
SLL = removeDuplicates(SLL)
SLL.display()
