import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    def symmetricTreeHelper(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        if left.val != right.val: return False
        return self.symmetricTreeHelper(left.left, right.right) and self.symmetricTreeHelper(left.right, right.left)
        
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.symmetricTreeHelper(root.left, root.right)

#test:
if __name__ == "__main__":
    root = build_tree_by_level([1,2,3,4,5,6,7])
    sol = Solution()
    print sol.isSymmetric(root)
    root2 = build_tree_by_level([1,2,2,3,3,3,3])
    print sol.isSymmetric(root2)
