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
        heapq.heappush(heap, ((nums1[0] + nums2[0], 0, 0)))
        while heap and len(result) <k :
            currentSum, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j +1< len(nums2):
                heapq.heappush(heap, ((nums1[i]+nums2[j+1], i, j+1)))
            if j == 0 and i + 1 < len(nums1):
                heapq.heappush(heap, ((nums1[i+1]+nums2[0], i+1, 0)))
        return result 
        
            
