class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return 
        if len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
                return
        #The tricky part is to think mathmatically why this is correct. 
        for i in xrange(0, len(nums) - 1):
            if i%2==0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i %2 ==1 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        #print nums
        return nums

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.wiggleSort([3, 5, 2, 1, 6, 4])
