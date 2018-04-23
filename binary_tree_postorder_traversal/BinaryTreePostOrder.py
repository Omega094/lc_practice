import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    
    def __init__(self):
        self.lst = []

    def recursiveTraversal(self, root):
        if root:
            self.recursiveTraversal(root.left)
            self.recursiveTraversal(root.right)
            self.lst.append(root.val)

    def iterativeTraversal(self, root):
        if not root: return 
        stack = [root]
        pre = None
        while stack:
            curr = stack[-1]
            if (not curr.right and not curr.left or (pre and (pre == curr.left or pre == curr.right) )):
                self.lst.append(curr.val)
                stack.pop()
                pre = curr
            else:
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
        return self.lst

    def postorderTraversal_elegant(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [(root, False)]
        self.lst = []
        while stack:
            node , visited = stack.pop()
            if node :
                if visited:
                    #When it is popped from stack at the second time, we traverse it.  
                    self.lst.append(node.val)
                    continue
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return self.lst 




#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7,8,9])
    sol.recursiveTraversal(root)
    print sol.lst
    sol.lst = []
    root = build_tree_by_level([1,2,3,4,5,6,7,8,9])
    print sol.iterativeTraversal(root)
    


