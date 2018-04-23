class Solution(object):

    def minCut(self, s):
        dp = [ 0 for i in range(len(s) + 1)]
        p = [[False for i in range(len(s))] for j in range(len(s))]
        #Assuming there is no palindrome existed in the string. 
        for i in range(len(s) + 1):
            dp[i] = len(s)  - i 
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and ((j - i) < 2 or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(1 + dp[j+1], dp[i])
        return dp[0] - 1

#test:
if __name__ == "__main__":
    s = "aab"
    sol = Solution()
    print sol.minCut(s)
