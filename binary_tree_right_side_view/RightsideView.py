# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    
    def __init__(self):
        self.solution  = []
    
    def traverseHelper(self, node, level):
        if node:
            if level > self.counter :
                self.solution.append(node.val)
                self.counter += 1
            self.traverseHelper(node.right, level+1)
            self.traverseHelper(node.left, level+1)
            
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.solution = []
        self.counter = 0
        self.traverseHelper(root, 1)
        return self.solution

    def rightSideView_stack(self, root):
        if root == None: return []
        stack = []
        stack.append(root)
        list = []
        while stack:
            nextStack = []
            list.append(stack[-1].val)
            for node in stack:
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            stack = nextStack
        return list


#test
if __name__ == "__main__":
    root = build_tree_by_level([1,2,3,4,5,6,7,8,9]) 
    pretty_print_tree(root, [])
    sol = Solution()
    print sol.rightSideView(root)




