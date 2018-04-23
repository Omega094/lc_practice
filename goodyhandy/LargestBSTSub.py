# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def checkValidBST(self, root):
        if root:
            if not root.left and not root.right:
                return (True, root.val, root.val, 1)
            leftCheck,leftMin, leftMax ,leftNum = self.checkValidBST(root.left)
            rightCheck, rightMin, rightMax, rightNum = self.checkValidBST(root.right)
            if leftCheck and rightCheck and root.val < rightMin and root.val > leftMax:
                if rightMax == float('-inf'): rightMax = root.val
                if leftMin == float('inf'): leftMin = root.val
                return (True, leftMin, rightMax ,leftNum + rightNum + 1)
            return (False, None, None, max(leftNum, rightNum))
        return (True, float('inf'), float('-inf') ,0)
    
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # print self.checkValidBST(root)
        # print self.checkValidBST(root.left)
        # print self.checkValidBST(root.right)
        return self.checkValidBST(root)[3]
        
