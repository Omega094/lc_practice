class Solution(object):
    def maximalRectangle(self, matrix):
        #use dynamic programming to calculate the histogram in
        #each row
        if not matrix: return 0
        width = len(matrix[0])
        height = len(matrix)
        table = [ [0 for i in xrange(width)] for j in xrange(height)]
        for i in range(0, width):
            table[0][i] = int( matrix[0][i] == "1")
        for y in range(1, height):
            for x in range(0, width):
                if matrix[y][x] == '0' :
                    table[y][x] = 0
                else:
                    table[y][x] = table[y-1][x] + 1
        return max([ self.largestRectangleArea(row) for row in table ])

    def largestRectangleArea(self, height):
        maxArea = 0
        height.append(0)
        currentIndex = 0
        stack = []
        while currentIndex < len(height):
            if (not stack) or height[currentIndex] >= height[stack[-1]] :
                stack.append(currentIndex)
                currentIndex += 1
            else:
                    leftHeightIndex = stack.pop()
                    maxArea = max(maxArea, height[leftHeightIndex]*(currentIndex if not stack else currentIndex - stack[-1] - 1))
        return maxArea

#test
if __name__ == "__main__":
    sol = Solution()
    board = ['01100','01100']
    print sol.maximalRectangle(board)