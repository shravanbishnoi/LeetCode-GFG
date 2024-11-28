"""
Palindrome:
Implement a function to check if a linked list is palindrome.
"""
from SinglyLinkedList import SinglyLinkedList
from Stack import Stack

def isPalindrom(sll):
    if sll.is_empty():
        return "SLL is empty"
    
    stack = Stack()
    slow = sll.head
    fast = sll.head.next
    while fast.next and fast.next.next:
        stack.push(slow.data)
        slow = slow.next
        fast = fast.next.next
    stack.push(slow.data)
    if fast.next:
        slow = slow.next
    slow = slow.next
    while slow:
        if slow.data != stack.pop():
            break
        slow = slow.next
    return stack.is_empty()
    
if __name__=='__main__':
    sll = SinglyLinkedList()
    lst = [2 , 1 , 4, -1, 4, 1, 2]
    for element in lst:
        sll.insert(element)
    sll.display()
    print(isPalindrom(sll=sll))
