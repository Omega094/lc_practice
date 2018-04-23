class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        from collections import Counter
        ctr = Counter(nums)
        result = []
        for num, freq in ctr.items():
            if len(result) < k or freq > result[0][0]:
                heapq.heappush(result, (freq, num))
            if len(result) > k:
                heapq.heappop(result)
        return map(lambda x: x[1], result)
        