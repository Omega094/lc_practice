class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        window = []
        result = []
        for i, num in enumerate(nums):
            while window and nums[window[-1]] <= num:
                window.pop()
            while window and i - window[0] >= k:
                window.pop(0)
            window.append(i)
            if i < k-1: continue
            result.append(nums[window[0]])
        return result
