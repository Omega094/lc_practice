class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        nums = set(nums)
        maxLen = 0
        while nums:
            current = nums.pop()
            currentLen = 1
            temp = current
            while temp + 1 in nums:
                nums.remove(temp + 1)
                temp += 1
                currentLen += 1
            temp = current
            while temp - 1 in nums:
                nums.remove(temp - 1)
                temp -= 1
                currentLen += 1
            maxLen = max(maxLen, currentLen)
        return maxLen
                
#test
sol = Solution()
print sol.longestConsecutive([100, 4, 200, 1, 3, 2])
