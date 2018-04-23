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
        def preOrder(root, lst):
            if root:
                lst.append(str(root.val))
                preOrder(root.left, lst)
                preOrder(root.right, lst)
                return
            lst.append("#")
            return 
        preOrder(root, result)
        return ",".join(result)
        
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        def deseHelper(lst):
            if lst[0] == "#":
                lst.pop(0)
                return None
            root = TreeNode(int(lst.pop(0)))
            root.left = deseHelper(lst)
            root.right = deseHelper(lst)
            return root
        return deseHelper(data)
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
