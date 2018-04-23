class Solution(object):
    
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        heightPerRow = [ [0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        heightPerRow[0] = map(int, matrix[0])
        for i in xrange(1, len(heightPerRow)):
            for j in xrange(len(heightPerRow[0])):
                if matrix[i][j] == '1':
                    heightPerRow[i][j] += heightPerRow[i-1][j] + 1
        return max([ self.largestRectangleArea(height) for height in heightPerRow])

    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans

#test
sol = Solution()
print sol.maximalRectangle(["10100","10111","11111","10010"])
