import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    
    def pathSumHelper(self, root, sum, numList, solutionList):
        #No need to allocate new list. 
        if not root : return
        if root and not root.left and not root.right:
            if root.val == sum: 
                numList.append(root.val)
                solutionList.append(numList[:])
                numList.pop()
                return
        nextSum = sum - root.val
        numList.append(root.val)
        self.pathSumHelper(root.left, nextSum, numList, solutionList)
        self.pathSumHelper(root.right, nextSum, numList, solutionList)
        numList.pop()
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        solutionList = []
        numList = []
        self.pathSumHelper(root, sum, numList, solutionList)
        return solutionList
#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    print sol.pathSum(root, 7)
