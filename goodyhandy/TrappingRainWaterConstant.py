class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #first Find the highes point index
        top = 0
        for i, num in enumerate(height):
            if num > height[top]:
                top = i
        #From left to right
        secondTop = 0
        totalWater = 0
        for i in xrange(top):
            if height[i] > height[secondTop]:
                secondTop = i
            totalWater += (height[secondTop] - height[i])
        #From left to right:
        secondTop = len(height) - 1
        for j in xrange(len(height) - 1, top, -1):
            if height[j] > height[secondTop]:
                secondTop = j
            totalWater += (height[secondTop] - height[j])
        return totalWater
