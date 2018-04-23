#It would be great to draw a matrix. 

import heapq
class Solution(object):

    def pushHeap(self,heap, i, j, l1, l2):
        if i < len(l1) and j < len(l2):
            heapq.heappush(heap, [l1[i] + l2[j], i, j])

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        self.pushHeap(heap, 0, 0, nums1, nums2)
        result = []
        while heap and len(result) < k:
            pairSum , i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            self.pushHeap(heap, i, j+1, nums1, nums2)
            if j == 0:
                self.pushHeap(heap, i+1, 0, nums1, nums2)
        return result

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.kSmallestPairs([1,7,11],  [2,4,6], 3)
