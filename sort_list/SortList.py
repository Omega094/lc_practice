import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    
    def merge(self, head1, head2):
        if head1 == None: return head2
        if head2 == None: return head1
        dummy = ListNode(0)
        p = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = head1
                head1 = head1.next
                p = p.next
            else:
                p.next = head2
                head2 = head2.next
                p = p.next
        if head1 == None:
            p.next = head2
        if head2 == None:
            p.next = head1
        return dummy.next
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #First Split
        if not head or not head.next:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        l1 = head
        l2 = slow.next
        slow.next = None
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return self.merge(l1, l2)

#test
if __name__ == "__main__":
    sol = Solution()
    l = construct_node_from_list([9,10,1,2,100,9,8,32,1])
    print l
    print sol.sortList(l)
