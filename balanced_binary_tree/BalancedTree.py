import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    
    def height(self,root):
        if not root: return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if abs(self.height(root.left) - self.height(root.right)) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,2,3,3,3,3,4,4])
    pretty_print_tree(root,[])
    print sol.isBalanced(root)
