class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumpCounter = 0
        currentStart = 0
        nextMax = nums[0]
        while currentStart < len(nums) -1 :
            temp = nextMax
            for i in xrange(currentStart, min(len(nums), nextMax + 1)):
                nextMax = max(nextMax, i + nums[i])
            currentStart = temp
            jumpCounter += 1
        return jumpCounter
        
