class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if i-1 >=0 and nums[i] == nums[i-1] : continue
            target = -num
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([num, nums[left], nums[right]])
                    left += 1; right -= 1
                    while left < right and nums[left] == nums[left-1] : left += 1
                    while left < right and nums[right] == nums[right+1]  : right -= 1
                elif nums[left] + nums[right] < target: 
                    left += 1
                else: 
                    right -= 1
        return result 
        
