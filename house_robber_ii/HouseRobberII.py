class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def robHelper(self, nums):
 
        money = [0 for i in xrange(len(nums))]
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
                money[i] = [money[i-1], money[i-2] + nums[i]] [money[i-1] <= money[i-2] + nums[i] ]
        return money[len(nums)-1]
        
    def rob(self, nums):
        if len(nums) == 1: return nums[0]
        if len(nums) == 0: return 0
        if len(nums) == 2: return max(nums[0], nums[1])
        #The answer is either the maxNum for not stealing the first house
        #or the maxNum for not stealing the last house.  =_=!!
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))
