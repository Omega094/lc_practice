import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head: return None
        counter = 0
        tempHead = head
        while tempHead != None:
            tempHead = tempHead.next
            counter += 1
        forwardStep = counter - n
        if forwardStep == 0 : return head.next
        tempHead = head
        for i in range (0, forwardStep - 1):
            tempHead = tempHead.next
        if tempHead.next:
            tempHead.next = tempHead.next.next
        return head

#test
if __name__ == "__main__":
    l2 = construct_node_from_list([1,2,3,4,5])
    sol = Solution()
    l1 = ListNode(1)
    print sol.removeNthFromEnd(l1,1)
    print sol.removeNthFromEnd(l2, 2)

