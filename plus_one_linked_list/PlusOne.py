# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        val = ""
        temp = head
        counter = 0
        while temp:
            val += str(temp.val)
            counter += 1
            temp = temp.next
        result = str(int(val) + 1)
        if len(result) > counter:
            newNode = ListNode(int(result[0]))
            newNode.next = head
            head = newNode
        iterator = iter(result)
        temp = head
        while temp:
            value = int(next(iterator))
            if temp.val != value:
                temp.val = value
            temp = temp.next
        return head

#test:
if __name__ == "__main__":
    sol = Solution()
    l1 = construct_node_from_list([9,9,9,9])
    print sol.plusOne(l1)
