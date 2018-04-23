import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    print sol.maxDepth(root)
