class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    class Node():
        def __init__(self, data, left=None, right=None) -> None:
            self.value = data
            self.left = left
            self.right = right

        def hasLeft(self):
            return self.left is not None

        def hasRight(self):
            return self.right is not None

        
    def is_empty(self):
        return self.size == 0
    
    def insert(self, data):
        new = self.Node(data)
        if self.is_empty():
            self.root = new
            self.size += 1
            return new

        current = self.root
        while current:
            if current.value <= new.value:
                if current.hasRight():
                    current = current.right
                else:
                    break
            else:
                if current.hasLeft():
                    current = current.left
                else:
                    break
        print(data)
        if current.value <= new.value:
            current.right = new
        else:
            current.left = new
        self.size += 1
        return new

    def print_levels(self, node, level=1):
        if node is None:
            return
        print(f'Node {node.value} is at level {level}')
        self.print_levels(node.left, level + 1)
        self.print_levels(node.right, level + 1)

arr = []
for i in range(30):
    arr.append(i)
bst = BinarySearchTree()
for item in arr:
    bst.insert(item)
bst.print_levels(bst.root)
