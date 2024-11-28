"""
Loop detection:
Given a circular linked list, implement an algorithm that returns True if a cycle is
present in SLL otherwise false.
DEFINITION: Circular linked list: A (currupt) linked list in which a node's next pointer
to an earlier node, so as to make a loop in the linked list.
"""

from SinglyLinkedList import SinglyLinkedList

def loopDetection(sll):
    if sll.is_empty():
        return "List is empty"
    
    slow = sll.head
    fast = sll.head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

sll = SinglyLinkedList()
lst = ['A', 'B', 'C', 'D', 'E']
for char in lst:
    sll.insert(char)

node_b = sll.head.next
node_e = sll.head.next.next.next.next
node_e.next = node_b

print(loopDetection(sll))
