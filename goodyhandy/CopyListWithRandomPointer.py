# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    
    def copyHelper(self, h, c, nodeMap):
        if h:
            if h.next:
                if h.next in nodeMap:
                    c.next = nodeMap[h.next]
                else:
                    c.next = RandomListNode(h.next.label)
                    nodeMap[h.next] = c.next
            if h.random:
                if h.random in nodeMap:
                    c.random = nodeMap[h.random]
                else:
                    c.random = RandomListNode(h.random.label)
                    nodeMap[h.random] = c.random
            self.copyHelper(h.next, c.next, nodeMap)
            
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        c = RandomListNode(head.label)
        nodeMap = {}
        nodeMap[head] = c
        self.copyHelper(head, c, nodeMap)
        return  c
