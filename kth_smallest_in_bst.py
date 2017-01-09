"""

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        counter = [0]
        value = [None]

        def inorder(node):
            if node.left is not None: inorder(node.left)
            counter[0] += 1
            if counter[0] == k: value[0] = node.val
            if node.right is not None: inorder(node.right)
        inorder(root)
        return value[0]
        
