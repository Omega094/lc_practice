
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    #The complexity is nlogn in worst case. n in average
    #This is a divide and conquer method. 
    def findKthLargest(self, nums, k):
        pivot = nums[0]
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot 

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.findKthLargest([3,2,1,5,6,4], 5)
