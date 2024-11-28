"""
List of depths:
Given a binary tree, design an algorithm which creates a
linked list of all the nodes at each depth. (e.g. if you have
a tree with depth D, you'll have D linked lists).
"""
from SinglyLinkedList import SinglyLinkedList
import queue
from BinaryTree import BinaryTree


def listOfDepths(root):
    if not root:
        return []

    result = []
    current_depth_list = SinglyLinkedList() 
    q = queue.Queue()
    q.put((root, 0)) 

    current_depth = 0
    while not q.empty():
        node, depth = q.get()

        if depth != current_depth:
            result.append(current_depth_list)
            current_depth_list = SinglyLinkedList()
            current_depth = depth
        
        current_depth_list.insert(node.val)

        if node.left:
            q.put((node.left, depth + 1))
        if node.right:
            q.put((node.right, depth + 1))

    result.append(current_depth_list)
    return result


if __name__ == '__main__':
    bt = BinaryTree()

    for i in range(1, 16):
        bt.insert(i)
    root = bt.get_root()
    depth_lists = listOfDepths(root)

    print("List of nodes at each depth:")
    for i, linked_list in enumerate(depth_lists):
        print(f"Depth {i}: ", end="")
        linked_list.display()