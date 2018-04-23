class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Top down DP 
        nums.append(1)
        nums.insert(0,1)
        table = [ [ 0 for _ in xrange(len(nums))] for _ in xrange(len(nums))]
        def dp(i, j):
            if table[i][j] != 0:
                return table[i][j]
            for x in xrange(i, j+1):
                table[i][j] = max(table[i][j], nums[x]*nums[i-1]*nums[j+1] + dp(i, x-1) + dp(x+1, j))
            return table[i][j]
        return dp(1, len(nums) - 2)
            
    def maxCoins_bottom_up(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1] # build the complete array 
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]
        for gap in xrange(2, n):
            for i in xrange(0, n - gap):
                j = i + gap
                for k in xrange(i+1, j ):
                    dp[i][j] = max(dp[i][j] , nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n-1]
