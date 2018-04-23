import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        preHead = ListNode(0)
        currentNode = preHead
        while (l1 and l2):
            if l1.val > l2.val:
                currentNode.next = l2
                l2 = l2.next
            else:
                currentNode.next = l1
                l1 = l1.next
            currentNode = currentNode.next
        if not l1:
            l1 = l2
        currentNode.next = l1
        return preHead.next

#test
if __name__ == "__main__":
    l1 = construct_node_from_list([1,3,5,7])
    l2 = construct_node_from_list([2,4,6,8])
    sol = Solution()
    print sol.mergeTwoLists(l1,l2)

