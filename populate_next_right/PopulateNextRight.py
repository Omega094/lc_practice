class Solution(object):
    
    def connectHelper(self, left, right):
        if left and right:
            left.next = right
            self.connectHelper(left.right, right.left)
        if left:
            self.connectHelper(left.left, left.right)
        if right:
            self.connectHelper(right.left, right.right)
        return
    
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root: return
        self.connectHelper(root.left, root.right)

    def connect_2(self, root):
        if root == None:
            return
        if root.left:
            root.left.next = root.right.next
        if root.right:
            if root.next == None:
                root.right.next = None
            else:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    def connect_smart(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root: return
        pre = root.left
        if not root.left and not root.right: return 
        while root and pre:
            if root.left and root.right:
                root.left.next = root.right
            if root.next and root.right and root.next.left:
                root.right.next = root.next.left
                root = root.next
            else:
                root = pre
                pre = root.left
