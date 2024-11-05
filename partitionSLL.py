"""
Partition:
Given a Singly Linked List and a value x, partition the SLL such that
all the elements less than x should appear before the x in SLL.

Example:
sll = 2 -> 1 -> 4 -> 4 -> 5 -> 6 -> 7 -> 8 -> 2 -> 3
x = 3
output:
2 -> 1 -> 2 -> 4 -> 5 -> 3 -> 4 -> 8 -> 6 -> 7

"""
from SinglyLinkedList import SinglyLinkedList

def partition(sll, x):
    if sll.is_empty():
        return "SLL is empty"
    current = sll.head
    while current.next:
        if current.next.data < x:
            node = current.next
            if current.next.next:
                current.next = current.next.next
            else:
                current.next = None
            node.next = sll.head
            sll.head = node
        else:
            current = current.next
    return sll
    
sll = SinglyLinkedList()
lst = [2 , 1 , 4 , 3, 4, -1, -2, 4, 10, 9, 2, 4, 5 , 6 , 7 , 8 , 2 , 3]
for element in lst:
    sll.insert(element)
sll.display()
sll_partitioned = partition(sll=sll, x=100)
sll_partitioned.display()