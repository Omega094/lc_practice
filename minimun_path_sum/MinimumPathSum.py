class Solution(object):

    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[ 0 for i in xrange(n)] for _ in xrange(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range (1, m):
            for j in range (1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]

#test:
if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 1, 0], [0, 1, 0], [1, 0 ,0]]
    print sol.minPathSum(grid)

