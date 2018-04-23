class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :
            return 0
        if len(nums) <= 2:
            return max(nums)
        tempMax = max(nums[1], nums[0])
        preTempMax = nums[0]
        for i in range(2, len(nums) ):
            tempMax , preTempMax= max(preTempMax + nums[i], tempMax), tempMax
        return tempMax

    def rob_non_constant_space(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :
            return 0
        if len(nums) <= 2:
            return max(nums)
        maxMoneyTable = [0 for _ in xrange(len(nums))]
        maxMoneyTable[0] = nums[0]
        maxMoneyTable[1] = max(nums[1], nums[0])
        tempMax = max(nums[1], nums[0])
        preTempMax = nums[0]
        for i in range(2, len(nums) ):
            temp = tempMax
            tempMax = max(preTempMax + nums[i], tempMax)
            preTempMax = temp
        return tempMax

#test:
if __name__ == "__main__":
    sol = Solution()
    test1 = [2,1,1,2]
    test2 = [1,3,1]
    print sol.rob(test1)

