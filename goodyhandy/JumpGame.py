class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach = 0
        for i, dist in enumerate(nums):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + dist)
            if maxReach >= len(nums): return True
        return True
