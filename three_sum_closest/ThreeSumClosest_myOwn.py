class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closestSum = float('inf')
        for i , num in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = num + nums[left] + nums[right]
                if threeSum == target: return threeSum
                if abs(target - threeSum) < abs(closestSum - target):
                    closestSum = threeSum
                if (num + nums[left] + nums[right]) < target:
                    left += 1
                else:
                    right -= 1
        return closestSum
