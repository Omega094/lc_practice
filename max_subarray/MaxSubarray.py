class Solution(object):

    #dp solution 
    def maxSubArray(self, nums):
        maxSumOnIndex = [None for _ in xrange(len(nums))]
        maxSumOnIndex[0] = nums[0]
        for i, num in enumerate (nums[1:], 1):
            maxSumOnIndex[i] = max(nums[i], maxSumOnIndex[i-1]+nums[i])
        return max(maxSumOnIndex)

    #dp constant space solution
    def maxSubArray_constant(self, nums):
        currentMax = nums[0]
        preCurrentMax = currentMax
        maxSubArraySum = nums[0]
        for i , num in enumerate(nums[1:], 1):
            preCurrentMax = currentMax 
            currentMax = max(nums[i], currentMax+nums[i])
            maxSubArraySum = max(maxSubArraySum, currentMax)
        return maxSubArraySum

    #no extra space, linear time. 
    def maxSubArray_no_extra_space(self, nums):
        for i, num in enumerate(nums[1:], 1):
            nums[i] = max(nums[i], nums[i-1]+nums[i])
        return max(nums)


#test 
if __name__ == "__main__":
    sol = Solution()
    print sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print sol.maxSubArray_constant([-2,1,-3,4,-1,2,1,-5,4])
    print sol.maxSubArray_no_extra_space([-2,1,-3,4,-1,2,1,-5,4])
