import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        if root.left:
            return 1 + self.minDepth(root.left)
        if root.right:
            return 1 + self.minDepth(root.right)
        return 1

#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    print sol.minDepth(root)
