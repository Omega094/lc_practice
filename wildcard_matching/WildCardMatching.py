class Solution(object):
    
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        if n - p.count('*') > m: return False   #avoid TLE
        dp = [[False for _ in xrange(len(p)+1)] for _ in xrange(len(s)+1)]
        dp[0][0] = True
        for i in range (1, len(p) + 1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
        for i in range (1, len(s) + 1):
            for j in range (1, len(p) + 1):
                if p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                #This is easier to come up with than regular expression matching. 
                    dp[i][j] = (dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1])
                else:
                    if p[j-1] == s[i-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False
        return dp[len(s)][len(p)]




#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.isMatch("aa","a")
    print sol.isMatch("aa","aa")
    print sol.isMatch("aaa","aa")
    print sol.isMatch("aa", "*")
    print sol.isMatch("aa", "a*")
    print sol.isMatch("ab", "?*")
    print sol.isMatch("aab", "c*a*b")
    
