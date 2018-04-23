import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    
    def reverseBetween(self, head, m, n):
        if m == n : return head 
        preHead = ListNode(0)
        preHead.next = head 
        front = preHead
        back = preHead
        for i in xrange(n):
            front = front.next
        for j in xrange(m-1):
            back = back.next
        #Save all endpoints that we need to 
        #reconnect. 
        preBack = back 
        back = back.next
        originBack = back 
        afterFront = front.next
        #now we need to reverse the segment. 
        tempPre = None 
        while back != front:
            tempNext = back.next
            back.next = tempPre
            tempPre = back 
            back = tempNext
        front.next = tempPre
        preBack.next = front
        originBack.next = afterFront
        return preHead.next

#test:
if __name__ == "__main__":
    sol = Solution()
    l1 = construct_node_from_list([1,2,3,4,5])
    print sol.reverseBetween(l1,2,4)

            
            
