# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    
    def copyHelper(self, node, copyNode, visited):
        if node:
            if node.next:
                if node.next in visited:
                    copyNode.next = visited[node.next]
                else:
                    copyNode.next = RandomListNode(node.next.label)
                    visited[node] = copyNode
                    self.copyHelper(node.next, copyNode.next, visited)
            if node.random:
                if node.random in visited:
                    copyNode.random = visited[node.random]
                else:
                    copyNode.random = RandomListNode(node.random.label)
                    visited[node.random] =  copyNode.random
            
    
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        visited = {}
        if not head: return None
        copyNode = RandomListNode(head.label)
        self.copyHelper(head, copyNode, visited)
        return copyNode
