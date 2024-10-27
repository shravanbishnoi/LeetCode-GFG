"""
Return kth to Last: Implement an algorithm to find the kth to last 
element of a singly linked list.
"""
from SinglyLinkedList import SinglyLinkedList

def kthToLast(sll, k):
    assert k>0, "K must be a positive int"
    if sll.is_empty():
        return "SLL is empty"
    elif sll.size < k:
        return "k must be greater than size of SLL"
    
    count = 0
    fast = sll.head
    while count <= k-1 and fast:
        count += 1
        fast = fast.next
    slow = sll.head
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.data

values = [2, 1, 4, -1, 5, 10, 11, 5, 3]
SLL = SinglyLinkedList()
for value in values:
    SLL.insert(value)
SLL.display()
node = kthToLast(SLL, 3)
print(node)
