class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or max(nums)-min(nums) == 0:   # in case bsize == 0
            return 0
        MAX = 1
        MIN = 0
        buckets = [[float('inf'), -float('inf')] for _ in xrange(len(nums) +1)]
        minNum = min(nums)
        maxNum = max(nums)
        bucketLen = len(nums)
        bucketDepth = (maxNum - minNum + 0.0)/bucketLen
        for i, num in enumerate(nums):
            location = int((num - minNum) / bucketDepth)
            buckets[location][MAX]  = max(num, buckets[location][MAX])
            buckets[location][MIN]  = min(num, buckets[location][MIN])
        pre = None
        maxGap = 0
        for minVal, maxVal in buckets:
            if not pre:
                pre = maxVal
                continue
            if minVal != float('inf') and maxVal != -float('inf'): 
                maxGap = max(maxGap, minVal - pre)
                pre = maxVal
        return maxGap
