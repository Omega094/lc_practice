"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
 
    def isSameTree(self, p, q):
        if not p and not q: return True
        if (not p or not q) or (p.val != q.val) : return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
 
    def isSubtree(self, T1, T2):
        # write your code here
        if not T2: return True
        if not T1: return False
        if T1.val == T2.val and self.isSameTree(T1, T2): return True
        return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
