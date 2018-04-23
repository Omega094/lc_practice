# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        preHead = ListNode(0)
        head = preHead
        import heapq
        heap = []
        for n in lists:
            if n :
                heapq.heappush(heap, (n.val, n))
        while heap:
            currentVal, currentNode = heapq.heappop(heap)
            head.next = currentNode
            head = head.next
            if currentNode.next:
                heapq.heappush(heap, (currentNode.next.val, currentNode.next))
        return preHead.next
        
        
