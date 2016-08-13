"""

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        array = []
        if root == None:
            return array
            
        else:
            self.initialArray(root, array)
        return array    
            
    def initialArray(self, root, array):
        array.append(root.val)
        if (root.left != None or root.right != None):
            if root.right != None:
                root = root.right
                #array.append(root.val)
                self.initialArray(root, array)
            else:
                root = root.left
                #array.append(root.val)
                self.initialArray(root, array)

                232887344:AAGKSC9o_Ax8HJ31lB_ApxMwoBj1O8tkMcQ