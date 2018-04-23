# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathHelper(self,root, prefixCounter, currentSum):
        if not root: return
        nextSum =currentSum+ root.val
        if prefixCounter[nextSum - self.target] != 0:
            self.count += prefixCounter[nextSum - self.target]
        prefixCounter[nextSum] += 1
        self.pathHelper(root.left, prefixCounter, nextSum)
        self.pathHelper(root.right, prefixCounter, nextSum)
        prefixCounter[nextSum] -= 1
        return 
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        prefixCounter = collections.Counter()
        self.target = sum
        self.count = 0
        prefixCounter[0] = 1
        self.pathHelper(root, prefixCounter, 0)
        return self.count
        
        
