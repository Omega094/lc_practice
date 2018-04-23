import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    
    def isValidBSTHelper(self, root, maxVal, minVal):
        if not root: return True
        if root:
            if root.val > maxVal or root.val < minVal:
                return False
            return self.isValidBSTHelper(root.left, root.val, minVal) and self.isValidBSTHelper(root.right, maxVal, root.val)

    def isValidBST(self, root):
        return self.isValidBSTHelper(root, float("inf"), -float("inf"))




    
