"""
Three in one:
Describe how could you use a singe array to implement three stacks
"""

class _Node(object):
    def __init__(self, data, prev=None) -> None:
        self._data = data
        self._prev = prev

class Stack(object):
    MAXSIZE = 15    

    def __init__(self) -> None:
        self.array = []
        self.s1 = self.SubStack()
        self.s2 = self.SubStack()
        self.s3 = self.SubStack()
    
    class SubStack:
        def __init__(self) -> None:
            self._top = None
            self._size = 0

        def _is_empty(self):
            return self._size == 0

    def push(self, stack_name, data):
        if len(self.array) == self.MAXSIZE:
            return "stack is full"
        
        stack = getattr(self, stack_name, None)
        if not stack:
            return "Invalid stack"

        newNode = _Node(data, stack._top)
        self.array.append(newNode)
        stack._top = newNode
        stack._size += 1
    
    def pop(self, stack_name):
        stack = getattr(self, stack_name, None)
        if not stack or stack._is_empty():
            return "stack is empty"
        
        top_node = stack._top
        stack._top = top_node._prev
        stack._size -= 1
        self.array.remove(top_node)
        return top_node._data


if __name__ == '__main__':
    s = Stack()
    print(s.s1._is_empty())
    print(s.push("s1", 1)) 
    print(s.s1._is_empty())
    print(s.push("s1", 2)) 
    print(s.push("s3", 3))
    print(s.push("s3", 4))  
    print(s.push("s2", 5)) 
    print(s.push("s1", 6))
    print(s.push("s1", 7))  
    print(s.push("s2", 8)) 
    print(s.push("s3", 9))
    print(s.push("s3", 1))  
    print(s.push("s2", 2)) 
    print(s.push("s1", 3))
    print(s.push("s3", 5))
    print(s.push("s1", 6))  
    print(s.push("s2", 7)) 
    print(s.push("s3", 2))  
    print(s.pop("s1"))
    print(s.pop("s1"))
    print(s.pop("s3"))
    print(s.pop("s3"))
    print(s.pop("s3"))
    print(s.s2._is_empty())
