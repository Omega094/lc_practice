import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next= head
        odd = head
        even = head.next
        temp = even
        while odd and even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = temp 
        return dummy.next
        
#test
if __name__ == "__main__":
    sol = Solution()
    l1 = construct_node_from_list([1,2,3,4,5,6,7,8])
    print sol.oddEvenList(l1)
