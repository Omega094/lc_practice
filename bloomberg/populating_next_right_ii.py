# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root: return
        pre = TreeLinkNode(0)
        tempPre = pre
        while root:
            while root:
                pre.next = root.left
                pre = pre.next or pre
                pre.next = root.right
                pre = pre.next or pre
                root = root.next
            root = tempPre.next
            pre = tempPre
            
