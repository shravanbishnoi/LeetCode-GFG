"""
Sum list: You have two numbers represented by a linked list,
where each node contains a single digit. The digits are stored in
reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as 
a linked list.

Example:
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 295.
Output: 2 -> 1 -> 9. That is 912.
"""

from SinglyLinkedList import SinglyLinkedList

def sumListNums(s1, s2):
    if s1.is_empty() or s2.is_empty():
        return "SLL is empty"
    
    count, num1, current = 0, 0, s1.head
    while current:
        num1 += current.data * (10**count)
        count += 1
        current = current.next

    count, num2, current = 0, 0, s2.head
    while current:
        num2 += current.data * (10**count)
        count += 1
        current = current.next
    total = int(str(num1 + num2)[::-1])
    result = SinglyLinkedList()
    while total > 0:
        digit = total % 10
        result.insert(digit)
        total = total // 10
    return result

print("Solving first problem:   ")
lst1 = [7, 1, 6]
lst2 = [5, 9, 2]
s1 = SinglyLinkedList()
s2 = SinglyLinkedList()

for i in range(len(lst1)):
    s1.insert(lst1[i])
    s2.insert(lst2[i])
print("Input: ")
s1.display()
s2.display()
total = sumListNums(s1, s2)
print("Output: ")
total.display()


### ----------- Follow up ------------------###
"""
Suppose the digits are stored in forward order. Repeat the above problem.
Example:
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5), That is 617 + 295
Output: 9 -> 1 -> 2, That is, 912.
"""

def sumListNums2(s1, s2):
    if s1.is_empty() or s2.is_empty():
        return "SLL is empty"
    
    count, num1, current = s1.size, 0, s1.head
    while current:
        num1 += current.data * (10**count)
        count -= 1
        current = current.next

    count, num2, current = s2.size, 0, s2.head
    while current:
        num2 += current.data * (10**count)
        count -= 1
        current = current.next
    total = int(str(num1 + num2)[::-1])
    result = SinglyLinkedList()
    while total > 0:
        digit = total % 10
        result.insert(digit)
        total = total // 10
    return result


print("\n\nSolving follow up problem:   ")
lst1 = [6, 1, 7]
lst2 = [2, 9, 5]
s1 = SinglyLinkedList()
s2 = SinglyLinkedList()

for i in range(len(lst1)):
    s1.insert(lst1[i])
    s2.insert(lst2[i])
print("Input: ")
s1.display()
s2.display()
total = sumListNums2(s1, s2)
print("Output: ")
total.display()