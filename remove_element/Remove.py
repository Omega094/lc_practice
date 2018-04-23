#Idea:
#Use a slow ptr, if num[i] is target, then we dont move the slow ptr
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        prev = 0
        for i , n in enumerate(nums):
            if nums[i] == val: continue
            nums[i], nums[prev] = nums[prev], nums[i]
            prev += 1
        return prev
