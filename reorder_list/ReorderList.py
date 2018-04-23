import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    
    def reverseList(self,head):
        pre = None
        while head:
            tempNext = head.next
            head.next = pre
            pre = head
            head = tempNext

        return pre

    def mergeNode(self, pre, follow):
        preForReturn = pre 
        while follow:
            tempPreNext = pre.next
            tempFollowNext = follow.next
            pre.next = follow
            follow.next = tempPreNext
            pre = tempPreNext
            follow = tempFollowNext
        return preForReturn
    

    def reorderList(self, head):
        if not head or not head.next:
            return head
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = slow.next
        slow.next = None
        tail = self.reverseList(tail)
        return self.mergeNode(head, tail)


#test
if __name__ == "__main__":
    l1 = construct_node_from_list([1,2,3,4])
    l2 = construct_node_from_list([1,2])
    l3 = construct_node_from_list([3])
    print l1
    sol = Solution()
    print sol.mergeNode(l2, l3)
    print sol.reverseList(l1)
    lFinal = construct_node_from_list([1,2,3,4,5,6,7])
    print sol.reorderList(lFinal), "This is the final result"
    lFinal2 = construct_node_from_list([1,2])
    print sol.reorderList(lFinal2)
