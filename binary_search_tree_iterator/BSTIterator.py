# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self._stack = []
        if root:
            self._stack.append(root)
            temp = root.left
            while temp:
                self._stack.append(temp)
                temp = temp.left
        return

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self._stack) > 0
        

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext(): return None
        returnNode = self._stack.pop()
        temp = returnNode.right
        while temp:
            self._stack.append(temp)
            temp = temp.left
        return returnNode.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
