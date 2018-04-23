class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        for i, num in enumerate(nums):
            left = i + 1
            right = len(nums) -1
            while left < right :
                if num + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count
        
