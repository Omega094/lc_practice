import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                leftResult = self.inorderSuccessor(root.left, p)
                if leftResult == None:
                    return root
                else:
                    return leftResult
        return None

    def inorderSuccessor_iter(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        #The inorder successor is the last node that is larger than p
        #therefore just "query" the binary tree. 
        succ = None
        while root:
            #The last one that is larger than p.val must be the successor of p
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ 

#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([3,1,4])
    pretty_print_tree(root,[])
    pretty_print_tree(sol.inorderSuccessor(root,root), [])
