class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return len(nums)
        back = 0
        for i in xrange(len(nums)):
            if nums[i] != nums[back]:
                back += 1
            if i != back:
                nums[back] = nums[i]
        return back + 1
            
                
        
