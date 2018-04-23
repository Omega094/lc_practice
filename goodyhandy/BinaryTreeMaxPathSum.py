# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def maxRootToLeafSum(self, root):
        if root:
            if not root.right and not root.left: return (root.val, root.val)
            lpn, lnpn = self.maxRootToLeafSum(root.left)
            rpn, rnpn = self.maxRootToLeafSum(root.right)
            cpn, cnpn = root.val, root.val
            cnpn = max(lnpn, 0, rnpn) + cnpn
            cpn = max(lpn, rpn, cpn + max(lnpn, 0)  + max(rnpn, 0))
            return (cpn, cnpn)
        return (-float("inf"), -float("inf"))

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxRootToLeafSum(root)[0]
