import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    
    def isLeaf(self, root):
        if root:
            return not root.left and not root.right
        return False

    def deleteLeaf(self, root, solution):
        if root:
            if root.left: 
                if self.isLeaf(root.left):
                    solution.append(root.left.val)
                    root.left = None
                else:
                    self.deleteLeaf(root.left, solution)
            if root.right:
                if self.isLeaf(root.right):
                    solution.append(root.right.val)
                    root.right = None
                else:
                    self.deleteLeaf(root.right, solution)
        return solution
        
        
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        parent = TreeNode(0)
        parent.right = root
        solutionList = []
        while parent.right:
            #The line below could be removed for submission.
            pretty_print_tree(parent.right, [])
            solution = self.deleteLeaf(parent,[] )
            if solution :
                solutionList.append(solution)
        return solutionList

if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    #pretty_print_tree(root, [])
    print sol.findLeaves(root)
