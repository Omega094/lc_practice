class Solution(object):
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
    print sol.largestRectangleArea([1,2,3,4,5])

