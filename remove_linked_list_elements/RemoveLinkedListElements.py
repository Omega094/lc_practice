# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        preHead = ListNode(0)
        preHead.next = head
        currentNode = preHead
        while currentNode and currentNode.next:
            while currentNode.next and currentNode.next.val == val:
                currentNode.next = currentNode.next.next
            currentNode = currentNode.next 
        return preHead.next

#test
#test
if __name__ == "__main__":
    l1 = construct_node_from_list([1,2,6,3,4,5,6])
    sol = Solution()
    print sol.removeElements(l1, 6)
