import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    
    def __init__(self):
        self.lst = []

    def inorderTraversal_recursive(self, root):
        if root:
            self.inorderTraversal_recursive(root.left)
            self.lst.append(root.val)
            self.inorderTraversal_recursive(root.right)
    
    def inorderTraversal_iterative(self, root):
        stack = []
        #Stack might be empty
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                self.lst.append(root.val)
                root = root.right 
        return self.lst 

    def inorderTraversal_morris(self, root):
        pre = None #The predecessor of each node
        while root != None :
            #If left is None, wisit current node and go right. 
            if root.left == None:
                self.lst.append(root.val)
                root = root.right
            else:
                #first find the predecessor of current node 
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right 
                #Point predecessor to current node
                if pre.right == None:
                    pre.right = root
                    root = root.left
                else:
                #In this case, pre.right has already been assigned
                # and that is the current node. so we should visit 
                #current node and recover the tree.
                    self.lst.append(root.val)
                    pre.right = None
                    root = root.right
        return self.lst


    
    def inorderTraversal(self, root):
        self.lst = []
        #self.inorderTraversal_recursive(root)
        #self.inorderTraversal_iterative(root)
        self.inorderTraversal_morris(root)
        return self.lst 

#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    print root.val
    print root.left.val
    print root.right.val
    pretty_print_tree(root,[])
    #print sol.inorderTraversal(root) 
