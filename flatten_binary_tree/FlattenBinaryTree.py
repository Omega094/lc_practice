import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self.flatten(root.left)
            self.flatten(root.right)
            if root.left:
                tempLeft = root.left
                tempRight = root.right
                root.right = root.left
                while tempLeft and  tempLeft.right:
                    tempLeft = tempLeft.right
                tempLeft.right = tempRight
                root.left = None
            return


#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    pretty_print_tree(root,[])
    sol.flatten(root)
    pretty_print_tree(root,[])

