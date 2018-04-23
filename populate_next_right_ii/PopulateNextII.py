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
