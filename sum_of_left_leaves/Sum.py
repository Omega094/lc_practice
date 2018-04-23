# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
 
    def leafHelper(self, root, isLeft):
        if root:
            if not root.left and not root.right: 
                if isLeft:
                    return root.val
            return self.leafHelper(root.left, True) + self.leafHelper(root.right, False)
        return 0
        
            
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.leafHelper(root, False)
        
