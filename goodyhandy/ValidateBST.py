# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def validateHelper(self, root, minVal, maxVal):
        if not root: return True
        if root.val <= minVal or root.val >= maxVal: return False
        return self.validateHelper(root.left, minVal, root.val) and self.validateHelper(root.right, root.val, maxVal)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        minVal = float('-inf')
        maxVal = float('inf')
        return self.validateHelper(root, minVal, maxVal)  
