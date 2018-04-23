#Need to think out of the box. 
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        backPtr = 0
        for num in nums:
            if num != 0:
                nums[backPtr] = num
                backPtr += 1
        for i in xrange(backPtr, len(nums)):
            nums[i] = 0
        return
