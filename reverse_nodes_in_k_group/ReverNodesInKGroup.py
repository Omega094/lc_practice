import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):

    #this helper returns reversed linked list with start and end node. 
    '''
    def reverseHelper(self, startNode, endNode):
        if not startNode.next or not startNode:
            return (startNode, startNode)
        tempStart, tempEnd = self.reverseHelper(startNode.next, endNode)
        startNode.next = None
        tempEnd.next = startNode
        return (tempStart, startNode)
    '''

    def reverse(self, start, end):
        newhead=None; newhead.next=start
        while newhead.next!=end:
            tmp=start.next
            start.next=tmp.next
            tmp.next=newhead.next
            newhead.next=tmp
        return [end, start]
        
    def reverseKGroup(self, head, k):
        if head==None: return None
        nhead=ListNode(0); nhead.next=head; start=nhead
        while start.next:
            end=start
            for i in range(k-1):
                end=end.next
                if end.next==None: return nhead.next
            res=self.reverse(start.next, end.next)
            start.next=res[0]
            start=res[1]
        return nhead.next


#test
if __name__ == "__main__":
    l1 = construct_node_from_list([1,2,3,4,5])
    sol = Solution()
    print sol.reverseKGroup(l1, 2)
#    end = l1;
#    while end.next :
#        end = end.next 
#    start , end =  sol.reverseHelper(l1, end)
#    print start
#    print end

