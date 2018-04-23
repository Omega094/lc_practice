# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Simply inorder traverse the tree and 
#once the minDist start to grwo we know that 
#the next node val is going to be more far away. 

class Solution(object):
    def closestValue_iterative(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        stack = []
        minDist = float('inf')
        closestVal = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val == target:
                    return int(target)
                if  abs(root.val - target) < minDist:
                    minDist = abs(root.val - target)
                    closestVal = root.val
                if abs(root.val - target) > minDist:
                    return int(closestVal)
                root = root.right 
        return int(closestVal)

    #This is recursive solution
    def closestValue(self, root, target):
        if root:
            if root.val == target:
                return int(target)
            if target < root.val:
                leftClosest = self.closestValue(root.left, target)
                if leftClosest == None: return root.val
                return int([root.val, leftClosest][int(abs(target - leftClosest) < abs(target - root.val))])
            else:
                rightClosest = self.closestValue(root.right, target)
                if rightClosest == None: return root.val
                return int([root.val, rightClosest][int(abs(target - rightClosest) < abs(target - root.val))])
        return None  
        
        
