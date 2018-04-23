class Solution(object):
    def numSquares(self, n):
        dp = [i for i in xrange(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in xrange(0, n+1):
            j = 1
            while i + j*j <= n:
                dp[i + j*j] = min(dp[i+j*j], dp[i] + 1)
                j += 1
        print dp
        return dp[-1]


#test
sol = Solution()
print sol.numSquares(13)
