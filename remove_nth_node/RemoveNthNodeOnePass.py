import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head: return None
        counter = 0
        preHead = ListNode(0)
        preHead.next = head
        fastNode = preHead; slowNode = preHead
        for i in range (0, n):
            fastNode = fastNode.next
        while fastNode.next:
            fastNode = fastNode.next
            slowNode = slowNode.next
        if slowNode.next:
            slowNode.next = slowNode.next.next
        return preHead.next

#test
if __name__ == "__main__":
    l2 = construct_node_from_list([1,2,3,4,5])
    sol = Solution()
    l1 = ListNode(1)
    print sol.removeNthFromEnd(l1,1)
    print sol.removeNthFromEnd(l2, 2)

