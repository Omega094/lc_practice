import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *


#Here are 3 approaches to solve the problem. 

class Solution(object):
    
    def __init__(self):
        self.prev = None

    #Worst case nlogn, but does not ned to traverse the whold tree
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        temp = root.left 
        while temp and temp.right:
            temp = temp.right
        if temp:
            if temp.val >= root.val:
                return False
        temp2 = root.right
        while temp2 and temp2.left:
            temp2 = temp2.left
        if temp2:
            if temp2.val <= root.val:
                return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    #worst case n, and does not need to traverse the whole tree. 
    def validBST(self, root, min, max):
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.validBST(root.left, min, root.val) and self.validBST(root.right, root.val, max)
    
    def isValidBST_ii(self, root):
        return self.validBST(root, -float('inf'), float('inf'))

    #We can also traverse the whole tree, and keep a global var to check if the traverse val is 
    #alwawy ascending. 
    
#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    pretty_print_tree(root)
    print "root: ", root.val, " root.left: ", root.left.val, " root.right: ", root.right.val
    print sol.isValidBST(root)
    print sol.isValidBST_ii(root)
