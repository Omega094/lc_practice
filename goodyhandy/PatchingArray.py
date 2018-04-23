class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        knownSum = 1
        i = 0
        count  = 0
        while knownSum <= n:
            if i < len(nums) and nums[i] <= knownSum:
                knownSum += nums[i]
                i += 1
            else:
                count += 1
                knownSum *= 2
        return count 
        
