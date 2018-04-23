class Solution(object):
    
    def dfsHelper(self, root, currentNum):
        if root:
            self.maxNum = max(self.maxNum, currentNum)
            if root.left and root.left.val == root.val + 1:
                self.dfsHelper(root.left, currentNum + 1)
            else:
                self.dfsHelper(root.left, 1)
            if root.right and root.right.val == root.val + 1:
                self.dfsHelper(root.right, currentNum + 1)
            else:
                self.dfsHelper(root.right, 1)
            
        
        
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxNum = 0
        self.dfsHelper(root, 1)
        return self.maxNum

