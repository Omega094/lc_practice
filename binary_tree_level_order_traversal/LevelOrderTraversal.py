import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
   
    def inorderTraversalHelper(self, root, level, lst):
        if not root: return
        if len(lst) <= level:
            lst.append([])
        lst[level].append(root.val)
        self.inorderTraversalHelper(root.left, level+1, lst)
        self.inorderTraversalHelper(root.right, level+1, lst)

    def levelOrder(self, root):
        lst = []
        level = 0
        self.inorderTraversalHelper(root, 0, lst)
        return lst

    def traverse(self, rootnode):
      thislevel = [rootnode]
      thisLevelList = [rootnode.val]
      self.list.append(thisLevelList)
      while thislevel:
        nextlevel = list()
        nextLevelList = []
        for n in thislevel:
          if n.left: 
              nextlevel.append(n.left)
              nextLevelList.append(n.left.val)
          if n.right: 
              nextlevel.append(n.right)
              nextLevelList.append(n.right.val)
        del thislevel
        thislevel = nextlevel
        if nextLevelList:
            self.list.append(nextLevelList)
#test:
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_by_level([1,2,3,4,5,6,7])
    print sol.levelOrder(root)

