import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q:
            if p.val != q.val:
                return False
        if not p or not q:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    print sol.isSameTree(root, root)
