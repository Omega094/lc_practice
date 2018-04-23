class Solution(object):
    
    #Bit trick, same as single number
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        result = 0
        for i in range(1, len(nums) + 1):
            result = result ^ i
            result = result ^ nums[i-1]
        return result
    
    #Math trick
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)/2 - sum(nums)
