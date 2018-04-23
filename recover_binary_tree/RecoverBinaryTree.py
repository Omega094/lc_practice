import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    
    def __init__(self):
        self.n1= None
        self.n2 = None
        self.pre = None

    def findSwappedNodes(self, root):
        if root:
            self.findSwappedNodes(root.left)
            if self.pre == None:
                self.pre = root
            else:
                if self.pre.val > root.val:
                    if not self.n1:
                        self.n1 = self.pre
                    self.n2 = root
                self.pre = root
            self.findSwappedNodes(root.right)


    def recoverTree(self, root):
        self.n1 = self.n2 = None
        self.pre = None
        self.findSwappedNodes(root)
        self.n1.val , self.n2.val = self.n2.val, self.n1.val

#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([2,3,1])
    print "Before recover: "
    pretty_print_tree(root, [])
    sol.recoverTree(root)
    print "After recorver: "
    pretty_print_tree(root, [])



