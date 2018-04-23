class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False for i in range(0, len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if s[j:i] in wordDict and dp[j] == True:
                    dp[i] = True
        return dp[len(s)] == True


#test
if __name__ == "__main__":
    s = "leetcode"
    wordDict = set(["leet", "code"])
    sol = Solution()
    print sol.wordBreak(s, wordDict)
