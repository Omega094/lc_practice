class Node(object):  # Please do not remove or rename any of this code
    """Represents a single node in the Ternary Search Tree"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.mid = None
        self.right = None

class Tree(object):  # Please do not remove or rename any of this code
    """The Ternary Search Tree"""
    def __init__(self):
        self.root = None

    # Please complete this method.
    """Inserts val into the tree. There is no need to rebalance the tree."""
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.insertHelper(self.root, val)
        return
    
    def insertHelper(self, root, val):
        if root.val == val:
            while root.mid:
                root = root.mid
            root.mid = Node(val)
            return
        if root.val > val:
            if not root.left:
                root.left = Node(val)
                return
            self.insertHelper(root.left, val)
        else:
            if not root.right:
                root.right = Node(val)
                return 
            self.insertHelper(root.right, val)
        return
        

    # Please complete this method.
    """Deletes only one instance of val from the tree.
       If val does not exist in the tree, do nothing.
       There is no need to rebalance the tree."""
    def delete(self, val):
        self.root = self.deleteHelper(self.root, val)
        return 
    
    def deleteHelper(self ,root, val):
        if not root: return None
        if root.val < val:
            root.right = self.deleteHelper(root.right, val)
        elif root.val > val:
            root.left = self.deleteHelper(root.left, val)
        else:
            if root.mid :
                root.mid = self.deleteHelper(root.mid, val)
                return root
            if not root.right:
                root = root.left
            else:
                nextNode = root.right
                while nextNode.left:
                    nextNode = nextNode.left
                root.val = nextNode.val
                root.right = self.deleteHelper(root.right, nextNode.val)
        return root
    
tree = Tree()
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.delete(8)
