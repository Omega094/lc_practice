import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

#We already know that this is a complete tree, 
#Therefore if we simply traverse the whole tree, 
#we will be getting a timeout. 

class Solution(object):
    #Complexity is nlogn ?
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0 
        hLeft = hRight = 0
        right = root
        left = root
        while right or left:
            if right:
                hRight += 1
                right = right.right
            if left:
                hLeft  += 1
                left = left.left
        if hRight == hLeft :
            return 2**hRight - 1
        return self.countNodes(root.right) + self.countNodes(root.left) + 1

    
    def countNodes_Fast(self, root):
        if not root:
            return 0
        hLeft = self.getDepthForCompleteTree(root.left)
        hRight = self.getDepthForCompleteTree(root.right)
        #If equal, that means left subtree is totally complete
        if hLeft == hRight:
            return 2**hLeft + self.countNodes_Fast(root.right)
        #If not equal, that means right subtree is a totally complete tree, 
        #with height 1 level than left subtree. 
        return 2**hRight + self.countNodes_Fast(root.left)

    def getDepthForCompleteTree(self, root):
        if not root:
            return 0
        return 1 + self.getDepthForCompleteTree(root.left)
