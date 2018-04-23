class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxWater = float('-inf')
        while left != right :
            maxWater = max(maxWater, (right - left)*min(height[right] , height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater
