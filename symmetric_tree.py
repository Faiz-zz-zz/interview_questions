"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        stack = [[root.left, root.right]]

        while len(stack):
            left, right = stack.pop()

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False

            if left.val == right.val:
                stack.append([left.right, right.left])
                stack.append([left.left, right.right])
            else:
                return False
        return True
