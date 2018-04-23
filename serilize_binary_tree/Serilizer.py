# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        def preorderHelper(root):
            if root:
                data.append(str(root.val))
                preorderHelper(root.left)
                preorderHelper(root.right)
            else:
                data.append("#")
        preorderHelper(root)
        return ",".join(data)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        iterator = iter(data.split(','))
        def preorderHelper(iterator):
            val = iterator.next()
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = preorderHelper(iterator)
            root.right = preorderHelper(iterator)
            return root
        return preorderHelper(iterator)
        


class Codec2:

    #Level order approach
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        queue = deque()
        queue.append(root)
        res = [root.val if root else "null"]
        while queue and queue[0] != None:
            node = queue.popleft()
            left = node.left
            right = node.right
            res.append(left.val if left else "null")
            res.append(right.val if right else "null")
            if left: queue.append(left)
            if right: queue.append(right)
        return ",".join(map(str, res))
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        from collections import deque
        nodes = deque()
        for val in data.split(","):
            if val != "null":
                nodes.append(TreeNode(int(val)))
            else:
                nodes.append(None)
        root = nodes.popleft()
        levelNode = deque([root])
        while levelNode:
            currentNode = levelNode.popleft()
            if currentNode:
                currentNode.left = nodes.popleft() if nodes else None
                currentNode.right = nodes.popleft() if nodes else None
                if currentNode.left: levelNode.append(currentNode.left)
                if currentNode.right: levelNode.append(currentNode.right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

#test:
if __name__ == "__main__":
    root = build_tree_by_level([1,2,3,4,5,6,7])
    pretty_print_tree(root, [])
    serilizer = Codec()
    print serilizer.serialize(root)
    serilizer2 = Codec2()
    print serilizer2.serialize(root)
