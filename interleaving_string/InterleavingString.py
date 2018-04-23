class Solution(object):

    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        lenS1 = len(s1)
        lenS2 = len(s2)
        dp = [[False for i in range(lenS1+1)] for j in range(lenS2+1) ]
        dp[0][0] = True
        for i in range(1, lenS1+1):
            dp[0][i] = (s1[i-1] == s3[i-1] and dp[0][i-1])
        for j in range(1, lenS2+1):
            dp[j][0] = (s2[j-1] == s3[j-1] and dp[j-1][0])
        for i in range(1, lenS2+1):
            for j in range(1, lenS1+1):
                dp[i][j] = (dp[i-1][j] and s2[i-1] == s3[i-1+j]) or (dp[i][j-1] and s1[j-1] == s3[i-1+j])
        return dp[lenS2][lenS1]


#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.isInterleave("aabcc","dbbca","aadbbcbcac")
    print sol.isInterleave("aabcc","dbbca","aadbbbaccc")

            
