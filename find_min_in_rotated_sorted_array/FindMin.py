class Solution(object):
 
    def findMin(self, nums):
        while len(nums) > 1 and nums[0] == nums[-1] : 
            nums.pop(0)
        if len(nums) == 1 : return nums[0]
        start = 0
        end = len(nums) - 1
        mid = (start + end) / 2
        pivotValue = nums[0] # This is the pivot value
        if nums[0]<= nums[-1]: return nums[0]
        while nums[mid+1] >= nums[mid]:
            if nums[mid] >= pivotValue: start = mid
            if nums[mid] <  pivotValue: end = mid
            mid = (start + end) / 2
        return nums[mid+1]

