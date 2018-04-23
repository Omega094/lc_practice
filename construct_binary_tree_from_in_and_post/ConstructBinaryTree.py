import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            #right first then left !!
            root.right = self.buildTree( inorder[ind+1:], postorder)
            root.left = self.buildTree (inorder[0:ind], postorder)
            return root

#test:
if __name__ == "__main__":
   inorder = [2,1,3]
   postorder = [2,3,1]
   sol = Solution()
   root = sol.buildTree(inorder,postorder)
   pretty_print_tree(root,[])
