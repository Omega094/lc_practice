class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numsSmaller = []
        numsBigger = []
        if not nums: return None
        pivot = nums[0]
        for num in nums:
            if num > pivot:
                numsBigger.append(num)
            if num < pivot:
                numsSmaller.append(num)
        if k <= len(numsBigger):
            return self.findKthLargest(numsBigger, k)
        if k > len(nums) - len(numsSmaller):
            #k - (len(nums) - len(numsSmaller)) are the number of elements that are
            #larger than or equal to the pivot !!!!!!
            return self.findKthLargest(numsSmaller, k - (len(nums) - len(numsSmaller)))
        return pivot

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.findKthLargest([3,2,1,5,6,4], 5)
