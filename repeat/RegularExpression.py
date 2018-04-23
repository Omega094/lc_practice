class Solution(object):
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        for i in range (1, len(p) + 1):
            if p[i-1] == '*':
                if i >= 2:
                    dp[0][i] = dp[0][i-2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == "*":
                    dp[i][j] = (dp[i-1][j] and (p[j-2]==s[i-1] or p[j-2]==".")) or dp[i][j-1] or dp[i][j-2]
                elif p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = (dp[i-1][j-1] and (s[i-1]==p[j-1]))
        return dp[len(s)][len(p)]
        




#test
if __name__ == "__main__":
    sol = Solution()
    print sol.isMatch("aa","a")
    print sol.isMatch("aa","aa")
    print sol.isMatch("aaa","aa")
    print sol.isMatch("aa", "a*")
    print sol.isMatch("aa", ".*")
    print sol.isMatch("ab", ".*")
    print sol.isMatch("aab", "c*a*b")
