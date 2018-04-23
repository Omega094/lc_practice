import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):

    def zigzagTraversalHelper(self, root, level, lst):
        if root:
            if len(lst) <= level:
                lst.append([])
            if level%2 == 0:
                lst[level].append(root.val)
            else:
                lst[level].insert(0,root.val)
            self.zigzagTraversalHelper(root.left, level+1,lst)
            self.zigzagTraversalHelper(root.right, level+1,lst)
            
    
    def zigzagLevelOrder(self, root):
        lst = []
        level = 0
        self.zigzagTraversalHelper(root, 0, lst)
        return lst

#test
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    print sol.zigzagLevelOrder(root)
