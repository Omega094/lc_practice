class Solution(object):

    #This solution got a time out. 
    #Needs O(n) solution
    def jump(self, nums):
        dp = [None for _ in xrange(len(nums))]
        dp[0] = 0
        maxReach = 0
        for i in range (0, len(nums)):
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= len(nums): return dp[i] + 1
            jumpCounter = dp[i]
            for j in range (i+1, maxReach+1):
                if j + nums[j] >= len(nums): return jumpCounter + 1
                if j < len(nums) and not dp[j]: dp[j] = jumpCounter+1
        return dp[-1]

#Elegant linear solution
#Greedy way
#Keep three variable
#currnetIndex, currentMax, nextMax
    def jumpLinear(self, nums):
        currentIndex = 0 #The index we are iterating one by one and to find the next max
        jumpCounter = 0
        nextMax = 0
        while nextMax  < len(nums)-1:
            currentMax = nextMax
            #Need to make sure we iterate every point till currentMax so we can find the largest nextMax
            while currentIndex <= currentMax :
                nextMax = max(nextMax, nums[currentIndex] + currentIndex)
                currentIndex += 1
            #update jumpcounter 
            jumpCounter += 1
        return jumpCounter


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.jump([2,3,1,1,4])
    print sol.jumpLinear([2,3,1,1,4])
    print sol.jumpLinear([5,9,3,2,1,0,2,3,3,1,0,0])
