import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    
    def maxPathSum(self, root):
        self.current_max = float('-inf')
        self.maxPathSumHelper(root)
        return self.current_max
    
    def maxPathSumHelper(self, root):
        if not root: return None
        left = self.maxPathSumHelper(root.left)
        right = self.maxPathSumHelper(root.right)
        left = 0 if left == None or left < 0 else left
        right = 0 if right == None or right < 0 else right
        self.current_max = max(self.current_max, root.val + left + right)
        return max(root.val + left, root.val + right, 0)


#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    pretty_print_tree(root, [])
    print sol.maxPathSum(root)