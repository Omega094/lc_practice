#O(n) time
#O(n) space

class Solution(object):
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        maxArea = 0
        for i , currentH in enumerate(height):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                #For each height, 
                #It's max area correspondent width is 
                #to the left most one that is higher than it and
                #to the right most one that is higher than it. 
                w = i - stack[-1] - 1
                maxArea = max(maxArea, h*w)
            stack.append(i)
        return maxArea

#test:
sol = Solution()
print sol.largestRectangleArea([2,1,5,6,2,3])
