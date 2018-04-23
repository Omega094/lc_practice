class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        prev = 0
        for i , n in enumerate(nums):
            if n != 0:
                nums[prev], nums[i] = nums[i], nums[prev]
                prev += 1
        return 
