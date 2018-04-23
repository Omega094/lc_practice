# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    def rob(self, root):
        return self.robHelper(root)[1];
        
    def robHelper(self,node):
        #The first element of tulpe saves the max money
        #gotten from not robbing the current node. 
        #The seconde element of tuple saves the solution for current
        #node 
        if not node :
            return (0, 0)
        leftResult = self.robHelper(node.left)
        rightResult = self.robHelper(node.right)
        return (leftResult[1] + rightResult[1], max(leftResult[1] + rightResult[1], node.val + leftResult[0]+rightResult[0])) 

#test
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7,8,9])
    pretty_print_tree(root, [])
    print sol.rob(root)
