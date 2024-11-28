"""
Validate BST: Implement a function to check if a binary tree
is binary search tree.
"""
from BinaryTree import BinaryTree

def validateBST(node, minVal=float('-inf'), maxVal=float('inf')):
    if node is None:
        return True
    if node.val >= maxVal or node.val <= minVal:
        return False
    return validateBST(node.left, minVal, node.val) and validateBST(node.right, node.val, maxVal)


 
if __name__=='__main__':
    bt = BinaryTree()

    bt.insert(6)
    bt.insert_left(6, 3)
    bt.insert_left(3, 2)
    bt.insert_left(2, 1)
    bt.insert_right(3, 4)
    bt.insert_right(4, 5)
    bt.insert_right(6, 9)
    bt.insert_left(9, 1)
    bt.insert_right(7, 8)
    bt.insert_right(9, 11)
    bt.insert_left(11, 10)

    root = bt.get_root()
    bt.in_order_traversal(root)
    print(validateBST(root))

    