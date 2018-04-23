#This is essentially a merge k sorted list problem
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        if not nums1 or not nums2: return []
        heap = []
        result = []
        for i in xrange(0, len(nums1)):
            heapq.heappush(heap, ((nums1[i] + nums2[0], i, 0)))
        while heap and len(result) <k :
            currentSum, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j +1< len(nums2):
                heapq.heappush(heap, ((nums1[i]+nums2[j+1], i, j+1)))
        return result 
        
            
