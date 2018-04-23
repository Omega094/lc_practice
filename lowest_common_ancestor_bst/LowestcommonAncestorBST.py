import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root:
            if root == p or root == q:
                return root
            left, right= self.lowestCommonAncestor(root.left,p,q), self.lowestCommonAncestor(root.right,p,q)
            if left and right : return root
            return left if left else right
    #Since it is BST, therefore we can use iterative
    def lowestCommonAncestor_iterative(self,root, p, q):
        while root:
            if root.val > max(p.val, q.val):
                root = root.left
            elif root.val < min(p.val, q.val):
                root = root.right
            else:
                return root
        return None

#test:

