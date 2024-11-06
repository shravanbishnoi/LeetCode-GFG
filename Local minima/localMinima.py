"""
In this script, there is an implementation for finding a local 
minima in a binary search tree. Where Local minima is defined as:
A node with the lowest value amongst its adjacent nodes.

Author: Shravan
Date: 27-Aug-2024
"""
class Node:
    """A class representing a Node"""

    def __init__(self, key, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.value = key

class BinaryTree(object):
    """A class representing a binary tree"""

    def __init__(self, rootValue=None) -> None:
        if rootValue is not None:
            self.root = Node(rootValue)
            self._size = 1
        else:
            self.root = None
            self._size = 0

    def __len__(self):
        return self._size

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self._size += 1
            return
        Q = [self.root]
        while Q:
            current = Q.pop(0)
            if current.left is None:
                current.left = Node(value)
                self._size += 1
                return
            else:
                Q.append(current.left)

            if current.right is None:
                current.right = Node(value)
                self._size += 1
                return
            else:
                Q.append(current.right)

    def has_children(self, node):
        return node.left is not None or node.right is not None

    def has_left(self, node):
        return node.left is not None

    def has_right(self, node):
        return node.right is not None

    def find(self, value):
        if self.root is None:
            return None
        Q = [self.root]
        while Q:
            current = Q.pop(0)
            if current.value == value:
                return current
            if current.left:
                Q.append(current.left)
            if current.right:
                Q.append(current.right)
        return None

    def localMinima(self, node):
        """Returns a local minima"""
        assert node is not None, "Node is none"
        # for leaf node
        if not self.has_children(node):
            return node.value
        # If only has left and not right child
        elif self.has_left(node) and not self.has_right(node):
            if node.value <= node.left.value:
                return node.value
            else:
                return self.localMinima(node.left)
        # If only has right but not left
        elif not self.has_left(node) and self.has_right(node):
            if node.value <= node.right.value:
                return node.value
            else:
                return self.localMinima(node.right)
        # Having both children
        else:
            if node.value <= node.left.value and node.value <= node.right.value:
                return node.value
            # recursively on left child
            elif node.left.value < node.value:
                return self.localMinima(node.left)
            else:
                return self.localMinima(node.right)


if __name__=='__main__':
    tree = BinaryTree(23)
    B = tree.insert(50)
    C = tree.insert(15)
    D = tree.insert(1)
    E = tree.insert(2)
    F = tree.insert(3)
    G = tree.insert(4)
    print(tree.localMinima(tree.root))
