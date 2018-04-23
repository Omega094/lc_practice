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
        tempPre = TreeLinkNode(0)
        pre = tempPre
        while root:
            while root:
                #Why cannot use pre.next = root.next or pre.next
                pre.next = root.left 
                pre = pre.next or pre
                pre.next = root.right 
                pre = pre.next or pre
                root = root.next
            root = tempPre.next
            pre = tempPre
