from collections import Counter
class Solution(object):
    def numDistinct(self, S, T):
        dp = [[0 for i in range(len(T)+1)] for j in range(len(S)+1)]
        for j in range(len(S)+1):
            dp[j][0] = 1
        for i in range(1, len(S)+1):
            for j in range(1, len(T)+1):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        #print dp
        return dp[len(S)][len(T)]

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.numDistinct("rabbbit", "rabbit")




