# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#global local 思想
class Solution(object):
    def robHelper(self, root):
        if not root:
            return (0, 0)
        leftG, leftL = self.robHelper(root.left)
        rightG, rightL = self.robHelper(root.right)
        G = max(leftG + rightG, root.val + leftL+ rightL)
        L = leftG + rightG
        return (G, L)

        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        g, l = self.robHelper(root)
        return g
        
