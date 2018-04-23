import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):

    def generateTreeHelper(self, start, end):
        if start > end: return [None]
        res = []
        for i in range(start, end+ 1):
            leftNodes = self.generateTreeHelper(start, i-1)
            rightNodes = self.generateTreeHelper(i+1, end)
            for leftNode  in leftNodes:
                for rightNode in rightNodes:
                    currentNode = TreeNode(i)
                    currentNode.left = leftNode
                    currentNode.right = rightNode
                    res.append(currentNode)
        return res


    def generateTrees(self, n):
        return self.generateTreeHelper(1, n)


#test:
if __name__ == "__main__":
    sol = Solution()
    trees = sol.generateTrees(3)
    print trees
    for tree in trees:
        pretty_print_tree(tree, [])
        print '//////'









