# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        def preorderHelper(root):
            if root:
                result.append(str(root.val))
                preorderHelper(root.left)
                preorderHelper(root.right)
            else:
                result.append("#")
        preorderHelper(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        from collections import deque
        data = deque(data.split(','))
        def preorderHelper(data):
            rootVal = data.popleft()
            if rootVal == "#": return None
            root = TreeNode(int(rootVal))
            root.left = preorderHelper(data)
            root.right = preorderHelper(data)
            return root
        return preorderHelper(data)
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
