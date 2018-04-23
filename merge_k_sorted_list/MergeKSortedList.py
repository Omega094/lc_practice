import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    def mergeTwoSortedList(self, l1, l2):
        preHead = ListNode(0)
        currentNode = preHead
        while l1 and l2:
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


    def mergeKLists_divideAndConquer(self, lists):
        #divide and conquer solution
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        if len(lists) == 2: return self.mergeTwoSortedList(lists[0], lists[1])
        mid = len(lists) / 2
        leftHalf = self.mergeKLists_divideAndConquer(lists[0:mid])
        rightHalf = self.mergeKLists_divideAndConquer(lists[mid:])
        return self.mergeTwoSortedList(leftHalf, rightHalf)

    #Need to push the val and node into heap
    def mergeKLists_heap(self, lists):
        import heapq
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap)
        preHead = ListNode(0)
        currentNode = preHead
        while heap:
            currentNode.next = heapq.heappop(heap)[1]
            if currentNode.next.next:
                heapq.heappush(heap, (currentNode.next.next.val , currentNode.next.next))
            currentNode = currentNode.next 
        return preHead.next
        

#test 
if __name__ == "__main__":
    l1 = construct_node_from_list([1,3,5,7])
    l2 = construct_node_from_list([2,4,6,8])
    l3 = construct_node_from_list([10,12,14,16])
    l4 = construct_node_from_list([11,13,15,17])
    lists = [l1,l2,l3,l4]
    sol = Solution()
    #print sol.mergeTwoSortedList(l1,l2)
    #print sol.mergeTwoSortedList(l3,l4)
    #a = sol.mergeKLists_divideAndConquer([l1,l2])
    #b = sol.mergeKLists_divideAndConquer(lists)
    #print b
    c = sol.mergeKLists_heap(lists)
    print c
