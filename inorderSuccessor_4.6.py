"""
Successor 4.6:
Write an algorithm to find the "next" node (i.e. in-order successor) of a given
node in a binary search tree. You may assume that each node has a link to its parent.
"""
def successor(node):
    if not node:
        return None
    
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current
    
    current = node
    while current.parent and current.parent.right == current:
        current = current.parent
    
    return current.parent
