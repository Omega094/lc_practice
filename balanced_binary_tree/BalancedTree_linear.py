# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#This is an O(n) solution !!!!!
class Solution(object):
    def height(self,root):
        if not root: return 0
        leftDepth = self.height(root.left)
        if leftDepth == -1 : return -1
        rightDepth = self.height(root.right)
        if rightDepth == -1 : return -1
        if abs(leftDepth-rightDepth) > 1: return -1
        return 1 + max(leftDepth, rightDepth)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.height(root) != -1
        
