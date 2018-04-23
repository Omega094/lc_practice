class Solution(object):
    def maxArea(self, heights):
        maxWater = 0
        left = 0; right = len(heights) - 1
        while left < right:
            maxWater = max( maxWater, min(heights[left] , heights[right]) * (right - left))
            if heights[left] < heights[right] : left += 1
            else: right -= 1
        return maxWater


            
#test: 
if __name__ == "__main__":
    sol = Solution()
    print sol.maxArea([1,1])
