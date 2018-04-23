class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        N = len(nums)
        sum = [0]
        for x in nums:
            sum += sum[-1] + x,
        
        # how many subarrays the array can be divided into such that no subarray has a sum larger than s
        def numSubarray(s):
            b = e = 0
            cnt = 0
            while e < N:
                while e < N and sum[e + 1] - sum[b] <= s:
                    e += 1
                cnt += 1
                b = e
            return cnt
      
        lo, hi = max(nums), sum[-1]
        while lo <= hi:
            mi = (lo + hi) / 2
            cnt = numSubarray(mi)
            if cnt <= m:
                hi = mi - 1
            else:
                lo = mi + 1
        return hi + 1
