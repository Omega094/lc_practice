import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *

class Solution(object):
    
    def reverseLinkedList(self, head):
        if not head:
            return None
        if not head.next: return head
        headNext = head.next
        reversedHead = self.reverseLinkedList(head.next)
        head.next = None
        headNext.next = head
        return reversedHead

    def reverseLinkedListIterative(self, head):
        if not head or not head.next: return None
        preCurrent = None
        currentNode = head
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = preCurrent
            preCurrent = currentNode
            currentNode = nextNode
        return preCurrent








#test
if __name__ == "__main__":
    l1 = construct_node_from_list([1,2,3,4])
    sol = Solution()    
    #print sol.reverseLinkedList(l1)
    print sol.reverseLinkedListIterative(l1)
