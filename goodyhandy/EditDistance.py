class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in xrange(len(word1) +1 )] for _ in xrange(len(word2) + 1)]
        for i in xrange(1 , len(word1) + 1):
            dp[0][i] = i
        for i in xrange(1, len(word2) + 1):
            dp[i][0] = i
        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                if word1[i-1] == word2[j-1] :
                    dp[j][i] = min(dp[j-1][i-1], dp[j-1][i]+1, dp[j][i-1]+1)
                else:
                    dp[j][i] = min(dp[j-1][i-1], dp[j-1][i], dp[j][i-1]) +1
        return dp[-1][-1]
