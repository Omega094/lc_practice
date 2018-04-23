class Solution(object):

    def numDecodings(self, s):
        if not s: return 0
        dp = [0 for i in xrange(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in xrange(2, len(s) + 1):
            if s[i-1] != '0': dp[i] = dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26: dp[i] += dp[i-2]
        return dp[len(s)]
            

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.numDecodings('12')
