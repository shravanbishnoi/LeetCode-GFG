"""
4.4: Check balanced:
Implement a function to check if a binary tree is balanced. For the purposes of this
question, a balanced tree is defined to be a tree such that the height of the two subtrees
of any node never differ by more than one.
"""
from BinaryTree import BinaryTree

def Height(node):
    if node is None:
        return 0
    return max(Height(node.left), Height(node.right)) + 1

def checkBalanced(root):
    if root.left and root.right:
        leftHeight = Height(root.left)
        rightHeight = Height(root.right)
        return abs(leftHeight - rightHeight) < 2
    return not(root.left.left)



if __name__ == '__main__':
    bt = BinaryTree()

    bt.insert(1)
    bt.insert_left(1, 2)
    bt.insert_left(2, 4)
    bt.insert_left(4, 5)
    bt.insert(3)
    # bt.insert_left(3, 6) # True

    root = bt.get_root()
    print(checkBalanced(root))