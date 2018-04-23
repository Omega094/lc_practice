class Solution(object):

    def trap(self, heights):
        #two pass dynamic programming. 
        if not heights or len(heights) == 1:
            return 0
        dpLeftHighest = [0 for _ in xrange(len(heights))]
        dpRightHighest = [0 for _ in xrange(len(heights))]
        #scan from left
        tempLeftHighest = 0
        for i, h in enumerate (heights):
            dpLeftHighest[i] = tempLeftHighest
            tempLeftHighest = max(h, tempLeftHighest)
        tempRightHighest = 0
        #We can directly accumulately computer max water in this water,
        #The third loop is not needed. 
        for i in range (len(heights)-1, -1, -1):
            dpRightHighest[i] = tempRightHighest
            tempRightHighest = max(heights[i], tempRightHighest)
        water = 0
        for i, h in enumerate (heights):
            water += max(0, (min(dpLeftHighest[i] , dpRightHighest[i]) - h ))
        return water

#test
if __name__ == "__main__":
    sol = Solution()
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    print sol.trap(heights)
