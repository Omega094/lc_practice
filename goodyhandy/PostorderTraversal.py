# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [(root, False)]
        result = []
        while stack:
            root , visited = stack.pop()
            if not visited:
                stack.append((root, True))
                if root.right:
                    stack.append((root.right, False))
                if root.left:
                    stack.append((root.left, False))
            else:
                result.append(root.val)
        return result
