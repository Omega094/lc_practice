class Solution(object):
    #Since the it is guaranteed to have valid result
    #Therefore the nth largth element is guaranteed to be larger than 
    #the n-half(length) th element
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        helper = sorted(nums)
        for i in xrange(1, len(nums), 2):
            nums[i] = helper.pop()
        for i in xrange(0, len(nums), 2):
            nums[i] = helper.pop()
        return nums


#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.wiggleSort([1, 5, 1, 1, 6, 4])
