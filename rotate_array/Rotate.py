class Solution(object):

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start  += 1
            end -= 1
        return 
    
    #Flip it then reverse
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        self.reverse(nums, 0,length - k - 1)
        self.reverse(nums, length-k, length-1)
        self.reverse(nums, 0, length-1)


#test
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol.rotate(nums, k)
    print nums
