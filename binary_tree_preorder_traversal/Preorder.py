import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):

    def __init__(self):
        self.lst = []

    def recursiveTraversal(self, root):
        if root:
            self.lst.append(root.val)
            self.recursiveTraversal(root.left)
            self.recursiveTraversal(root.right)


    def iterativeTraversal(self, root):
        stack = []
        while stack or root:
            while root:
                print root.val, "root into stack"
                self.lst.append(root.val)
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                print root.val, "root out from stack"
            root = root.right

        return self.lst 

    def iterativeTraversal_elegant(self, root):
        stack = [root]
        while stack:
            root = stack.pop()
            if root :
                self.lst.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
        return self.lst
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.lst = []
        return self.iterativeTraversal(root)
#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7,8,9])
 
    pretty_print_tree(root,[])
    print sol.preorderTraversal(root)

