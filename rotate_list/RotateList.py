import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):

    def rotateRight(self, head, k):
        #Two pointer approach. 
        if not head or not head.next: return head
        preHead = ListNode(0)
        preHead.next = head
        #k might be larger than the size of the list. 
        counter = 0
        while head :
            counter += 1
            head = head.next
        head = preHead.next
        k = k % counter 
        if k == 0: return head 
        front = head 
        for i in xrange(k):
            front = front.next
        back = head 
        while front.next :
            front = front.next
            back = back.next
        preHead.next = back.next
        front.next = head
        back.next = None
        return preHead.next

#test 
if __name__ == "__main__":
    sol = Solution()
    lst = construct_node_from_list([1,2,3,4,5])
    lst2 = construct_node_from_list([1,2])
    print sol.rotateRight(lst, 7)
    print sol.rotateRight(lst2, 2)

