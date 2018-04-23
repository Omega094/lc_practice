class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s1 = float('inf')
        s2 = float('inf')
        for num in nums:
            if num <= s1:
                s1 = num
            elif num <= s2:
                s2 = num
            else:
                return True
        return False
        
