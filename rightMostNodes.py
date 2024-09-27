"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
"""
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        lst = []
        queue = [root]
        while queue:
            length = len(queue)
            rightmost = None
            for i in range(len(queue)):
                node = queue.pop(0)
                rightmost = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            lst.append(rightmost.val)
        return lst

