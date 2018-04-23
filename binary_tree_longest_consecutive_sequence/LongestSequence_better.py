# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if not root: return 0, 0
        leftG, leftL = self.helper(root.left)
        rightG, rightL = self.helper(root.right)
        currentL = 1
        if root.left and root.val + 1 == root.left.val :
            currentL =max(currentL, leftL + 1)
        if root.right and root.val + 1 == root.right.val :
            currentL = max(currentL, rightL + 1)
        currentG = max(currentL, leftG, rightG)
        return currentG, currentL
        
        
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        if not root: return 0
        return self.helper(root)[0]
        
        
