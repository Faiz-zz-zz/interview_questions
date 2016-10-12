# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]
        def recurMethod(node):
            count[0] += 1
            if node.left != None:
                recurMethod(node.left)
            elif node.right != None:
                recurMethod(node.right)

        recurMethod(root)
        return count[0]            
