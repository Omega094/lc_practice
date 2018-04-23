import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    def swapPairs(self, head):
        if not head: return None
        preHead = ListNode(0)
        preHead.next = head
        tempPre = preHead
        while  tempPre.next:
            first = tempPre.next 
            second = first.next
            if not second: break
            third = second.next
            #Here is the swapping
            tempPre.next = second
            second.next = first
            first.next = third
            ####################
            #point to the curent "second"
            tempPre = first 
        return preHead.next

#test
if __name__ == "__main__":
    l1 = construct_node_from_list([1,2,3,4])
    sol = Solution()
    print sol.swapPairs(l1)
 
