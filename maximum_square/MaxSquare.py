class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = [ [0]*len(matrix[0]) for i in xrange(len(matrix))]
        if not matrix : return 0
        maxSideLength = 0
        for i in range(0, len(matrix)):
            dp[i][0] = int( matrix[i][0] )
            maxSideLength = max(maxSideLength, dp[i][0])
        for j in range(0, len(matrix[0])):
            dp[0][j] = int(matrix[0][j])
            maxSideLength = max(maxSideLength, dp[0][j])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if int(matrix[i][j]) == 1:
                    #Only right when the grid is 1, otherwise dp[i][j] should be 0 !!!!
                    dp[i][j] = min (dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + int(matrix[i][j])
                else:
                    dp[i][j] = 0
                maxSideLength = max(maxSideLength, dp[i][j])
        return maxSideLength**2

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.maximalSquare(["101101","111111","011011","111010","011111","110111"])
