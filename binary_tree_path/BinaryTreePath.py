import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePathHelper(self, root, currentStr, solutionList):
        if root:
            currentStr = currentStr  + str(root.val) + "->"
            if not root.left and not root.right :
                solutionList.append(currentStr[:-2])
                return 
            self.binaryTreePathHelper(root.left, currentStr, solutionList)
            self.binaryTreePathHelper(root.right, currentStr, solutionList)
        return 
        
    def binaryTreePaths(self, root):
        if not root:
            return []
        currentStr = ""
        solutionList = []
        self.binaryTreePathHelper(root, currentStr, solutionList)
        return solutionList

#test
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7,8,9])
    pretty_print_tree(root, [])
    print sol.binaryTreePaths(root)
