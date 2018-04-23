# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *


#We can achieve recursive with complexity k 
#We can also iteratively traverse it . 
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.counter = 0
        return self.inorderTraverseHelper(root, k)
    
    def inorderTraverseHelper(self, root, k):
        if root:
            leftResult = self.inorderTraverseHelper(root.left, k)
            if leftResult != None : return leftResult
            self.counter += 1
            if self.counter == k:
                return root.val
            return self.inorderTraverseHelper(root.right, k)
    
    def kthSmallest_Iterative(self, root, k):
        stack = []
        stack.append(root)
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k -= 1
                if k == 0:
                    return root.val
                root = root.right
        return None


#test
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([5,4,6])
    pretty_print_tree(root, [])
    print sol.kthSmallest(root, 2)
    print sol.kthSmallest_Iterative(root, 2)
