# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):

    def dfsCopy(self, node, newNode, visited):
       if node: 
            if node.next:
                if node.next.label in visited:
                    newNode.next = visited[node.next.label]
                else:
                    newNode.next = RandomListNode(node.next.label)
                    visited[node.next.label] = newNode.next
            #now we need to copy random
            if node.random:
                if node.random.label in visited:
                    newNode.random = visited[node.random.label]
                else:
                    newNode.random = RandomListNode(node.random.label)
                    visited[node.random.label] = newNode.random
            if node.next:
                self.dfsCopy(node.next, newNode.next, visited)

    def copyRandomList(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        visited = dict()
        if not node : return None
        resultNode = RandomListNode(node.label)
        visited[node.label] = resultNode
        self.dfsCopy(node, resultNode, visited)
        return resultNode
