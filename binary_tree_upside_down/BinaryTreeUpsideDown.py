import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            if not root.left and not root.right : return root
            left = root.left
            right = root.right
            parent = root
            newNode = self.upsideDownBinaryTree(left)
            rightMost = newNode
            while rightMost.right:
                rightMost = rightMost.right
            # if right:
            #     rightMost.left = right
            # rightMost.right = TreeNode(parent.val)
            rightMost.left = right
            rightMost.right = TreeNode(parent.val)
            return newNode
            
        return None

#test
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7,8,9])

    pretty_print_tree(root,[])
    newRoot = sol.upsideDownBinaryTree(root)
    pretty_print_tree(newRoot, [])
