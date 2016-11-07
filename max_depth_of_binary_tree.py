"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from
 the root node down to the farthest leaf node.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recurMethod(node):
            if node is None:
                return 0

            if node.right is None and node.left is None:
                return 1

            left, right = 0, 0

            if node.left is not None:
                left = recurMethod(node.left)

            if node.right is not None:
                right = recurMethod(node.right)

            return 1 + max(left, right)
        return recurMethod(root)
