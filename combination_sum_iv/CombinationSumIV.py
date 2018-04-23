class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        table = [0 for _ in xrange(target+1)]
        nums.sort()
        numSet = set(nums)
        if target < nums[0] : return 0
        table[nums[0]] = 0
        for i in xrange(nums[0], target + 1):
            if i in numSet:
                table[i] += 1
            for j in nums:
                if j > i: break
                table[i] += table[i - j]
        return table[target]

#Test
sol = Solution()
print sol.combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10)
