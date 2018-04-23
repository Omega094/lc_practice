class Solution(object):
    def canJump(self, nums):
        maxReach = 0
        for i in range (0, len(nums)):
            #This means we cannot reach the end
            #Directly return false
            if i > maxReach: return False
            maxReach = max(maxReach, nums[i] + i)
        return maxReach >= len(nums) - 1


#test 
if __name__ == "__main__":
    sol = Solution()
    print sol.canJump([2,3,1,1,4])
    print sol.canJump([3,2,1,0,4])

