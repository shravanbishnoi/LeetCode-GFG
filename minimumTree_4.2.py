"""
4.2: Minimum Tree
Given a sorted array of distinct integers
Write a algo to construct a BST with minimum 
height.
"""

from BST import BinarySearchTree

def minimumTree(arr):
    if len(arr) == 0:
        return "List is empty"
    
    n = len(arr)-1
    count = 0
    while count < n:
        




arr = []
for i in range(30):
    arr.append(i)
bst = BinarySearchTree()
for item in arr:
    bst.insert(item)
bst.print_levels(bst.root)
