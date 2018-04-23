
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def isUnivalTree(self,root):
        if not root:
            return True
        if not root.right and not root.left:
            return True
        if self.isUnivalTree(root.left) and self.isUnivalTree(root.right):
            if root.right and root.left:
                return root.left.val == root.right.val== root.val
            if root.right :
                return root.val == root.right.val
            if root.left:
                return root.val == root.left.val
        return False
            
    def traverseHelper(self, root):
        if root:
            left = self.traverseHelper(root.left)
            right = self.traverseHelper(root.right)
            return 1 + left + right 
        return 0
     
    
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if self.isUnivalTree(root): return self.traverseHelper(root)
        else:
            return self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right)
        
        
        
        
