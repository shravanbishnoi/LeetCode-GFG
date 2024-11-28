"""
This script contains Node based implementation of stack
"""
import math

class Stack(object):

    class Node(object):

        def __init__(self, data, next=None):
            self._data = data
            self.next = next

    def __init__(self):
        self._top = None
        self.size = 0
        self._min_elements = []

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        newNode = self.Node(value)
        newNode.next = self._top
        self._top = newNode
        self.size += 1
        if not self._min_elements:
            self._min_elements.append(value)
        else:
            current_min = self._min_elements[-1]
            self._min_elements.append(min(current_min, value))

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        value = self._top._data
        self._top = self._top.next
        self.size -= 1
        self._min_elements.pop()
        return value

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self._top._data

    def min(self):
        if self.is_empty():
            return "Stack is empty"
        return self._min_elements[-1]

    def max(self):
        if self.is_empty():
            return "Stack is empty"
        max_element = -math.inf
        current = self._top
        while current:
            if current._data > max_element:
                max_element = current._data
            current = current.next
        return max_element

    def sort(self):
        if self.is_empty():
            return "Stack is empty"

        sorted_stack = Stack()
        temp_stack = Stack()

        while not self.is_empty():
            max_element = self.max()

            while not self.is_empty():
                element = self.pop()
                if element == max_element:
                    sorted_stack.push(max_element)
                else:
                    temp_stack.push(element)

            while not temp_stack.is_empty():
                self.push(temp_stack.pop())

        return sorted_stack

if __name__ == '__main__':
    s = Stack()
    elements = [3, 1, 4, 2, 5 ,6 , 6 ,7, 100, 4, 3, 2, 1]
    for elem in elements:
        s.push(elem)
        print(f"Pushed --> {elem}")

    print("Max element:", s.max())

    sorted_stack = s.sort()
    print("Sorted elements:")
    while not sorted_stack.is_empty():
        print("Popped from sorted stack -->", sorted_stack.pop())
