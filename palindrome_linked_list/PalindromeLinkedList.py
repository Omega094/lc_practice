import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head is None:
            return True
        #find mid node
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #reverse second half
        p, last = slow.next, None
        slow.next = None #not needed, but clearer
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        #check palindrome
        p1, p2 = last, head
        while p1 :
            if not (p1.val == p2.val): return False
            p1, p2 = p1.next, p2.next
        return True

