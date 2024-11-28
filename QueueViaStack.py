"""
Queue via stack:
Implement MyQueue class which implements a queue using two stacks.
"""
from Stack import Stack

class MyQueue:

    def __init__(self) -> None:
        self._enqueueStack = Stack()
        self._dequeueStack = Stack()

    def is_empty(self):
        return self._enqueueStack.is_empty() and self._dequeueStack.is_empty()
    
    def enqueue(self, value):
        self._enqueueStack.push(value)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        
        if self._dequeueStack.is_empty():
            while not self._enqueueStack.is_empty():
                self._dequeueStack.push(self._enqueueStack.pop())
        
        return self._dequeueStack.pop()

    def size(self):
        return self._enqueueStack.size + self._dequeueStack.size


if __name__ == '__main__':
    Q = MyQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    print("Queue size:", Q.size())
    print("Is queue empty?", Q.is_empty())
    print("Dequeue:", Q.dequeue())
    print("Dequeue:", Q.dequeue())
    print("Queue size:", Q.size())
    print("Dequeue:", Q.dequeue())
    print("Is queue empty?", Q.is_empty())
    print("Dequeue:", Q.dequeue())
