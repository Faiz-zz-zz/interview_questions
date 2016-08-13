"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        absMin = -sys.maxsize
        sumPath = [absMin]

        def maxSolution(root, sumPath):
        	if root == None:
        		return 0

        	left = absMin

        	if root.left != None:
        		left = maxSolution(root.left, sumPath)

        	right = absMin

        	if root.right != None:
        		right = maxSolution(root.right, sumPath)

        	thisNode = max(root.val, right + root.val, left + root.val)
        	
        	sumPath[0] = max(sumPath[0], thisNode, left + right + root.val)

        	return thisNode
        a = maxSolution(root, sumPath)	
        return sumPath[0]			