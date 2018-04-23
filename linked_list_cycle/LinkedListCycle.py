class Solution(object):
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     hashSet = set()
    #     while head:
    #         if head in hashSet:
    #             return True
    #         hashSet.add(head)
    #         head = head.next
    #     return False

    def hasCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
