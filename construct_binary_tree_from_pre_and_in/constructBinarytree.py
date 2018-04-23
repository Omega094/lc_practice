import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            #inorder gets exhausted faster than preorder. 
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root 




#test:
if __name__ == "__main__":
   preorder = [1,2]
   inorder = [2,1]
   sol = Solution()
   root = sol.buildTree(preorder, inorder)
   pretty_print_tree(root,[])
