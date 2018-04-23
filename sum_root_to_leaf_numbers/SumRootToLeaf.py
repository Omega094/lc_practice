import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    
    def __init__(self):
        self._sum = 0

    def traverseHelper(self, currentSum, root):
        if root:
            currentSum += root.val
            if not root.right and not root.left:
                self._sum += currentSum
            self.traverseHelper(currentSum*10, root.left)
            self.traverseHelper(currentSum*10, root.right)




    def sumNumbers(self, root):
        self.traverseHelper(0, root)
        return self._sum

#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    pretty_print_tree(root, [])
    print sol.sumNumbers(root)
