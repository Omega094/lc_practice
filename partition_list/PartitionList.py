import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        smallerPreHead = ListNode(0)
        largerPreHead = ListNode(0)
        currentSmallerHead = smallerPreHead
        currentLargerHead = largerPreHead
        current = head
        if not head or not head.next:
            return head
        while current  :
            if current.val < x:
                currentSmallerHead.next = current
                currentSmallerHead =currentSmallerHead.next
            else:
                currentLargerHead.next = current
                currentLargerHead = currentLargerHead.next
            current = current.next
        currentSmallerHead.next = largerPreHead.next
        #need this line to avoid circle.
        currentLargerHead.next = None 
        return smallerPreHead.next

if __name__ == "__main__":
    sol = Solution()
    l1 = construct_node_from_list([1,4,3,2,5,2])
    head = sol.partition(l1, 3)
    print head
