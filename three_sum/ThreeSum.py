#Space O(1)
#Time O(nlogn)
#Note we need to do two skipping optimizaion. 

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #first action: sort.
        nums.sort()
        solution = []
        for i, num in enumerate(nums[:-2]):
            #start using two pointers.
            if i == 0 or nums[i] > nums[i-1]:
                left  = i + 1
                right = len(nums)-1
                target = -num
                while left < right:
                    sum = nums[left] + nums[right]
                    if sum == target:
                        solution.append([num, nums[left], nums[right]])
                        left += 1; right -= 1
                        #Skip same number
                        while left < right and nums[left] == nums[left-1] : left += 1
                        while left < right and nums[right] == nums[right+1]  : right -= 1
                    #optimization here again by skipping impossible candidate
                    while left < right and  target < nums[left] + nums[right]: right -= 1
                    while left < right and target > nums[left] + nums[right]: left += 1
        return solution
        
        
