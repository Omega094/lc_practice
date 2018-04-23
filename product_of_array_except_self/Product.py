class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        if len(nums) < 2: return nums
        productFromLeft = [0]*len(nums)
        productFromLeft[0] = nums[0]
        for i in xrange(1, len(nums)-1):
            productFromLeft[i] = nums[i] * productFromLeft[i-1]
        productFromRight = [0]*len(nums)
        productFromRight[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            productFromRight[i] = productFromRight[i+1]*nums[i]
        result = [None]*len(nums)
        result[0] = productFromRight[1]
        result[-1] = productFromLeft[-2] 
        for i in xrange(1, len(nums)-1):
            result[i] = productFromRight[i+1]*productFromLeft[i-1]
        return result

    def productExceptSelf_better_space(self, nums):
        if len(nums) < 2: return nums

        ret = [0 for i in xrange(len(nums))]

        '''
        From left to right, construct left-prodcut
        array, i.e., ret[i] = product(nums[0]...nums[i])
        '''
        ret[0] = nums[0]
        for i in xrange(1,len(nums)-1):
            ret[i] = nums[i] * ret[i-1]

        # The right product beyond current index
        rt = 1

        '''
        From right to left, ret[i] = ret[i-1] * rt
        '''
        for i in xrange(len(nums) - 1, 0, -1):
            ret[i] = ret[i-1] * rt
            rt *= nums[i]
        ret[0] = rt   

        return ret
#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.productExceptSelf([1,2,3,4])
