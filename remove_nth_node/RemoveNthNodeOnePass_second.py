# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        preHead = ListNode(0); preHead.next = head
        preSlow = preHead
        fast = preHead
        slow = preHead
        for i in xrange(n):
            fast = fast.next
        while  fast.next:
            fast = fast.next
            slow = slow.next
            preSlow = preSlow.next
        if  preSlow.next.next:
            preSlow.next = preSlow.next.next
        else:
            preSlow.next = None
        return preHead.next
        
