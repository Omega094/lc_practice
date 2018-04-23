class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f, s, t = nums[0], float('-inf'), float('-inf')
        for n in nums[1:]:
            if n > f:
                t = s
                s = f
                f = n
            elif n > s and n < f:
                t = s
                s = n
            elif n > t and n < s:
        return t if t != float('-inf') else  f
        
