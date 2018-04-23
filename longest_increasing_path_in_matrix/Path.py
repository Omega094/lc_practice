class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfsHelper(x, y):
            if y < 0 or y >= height or x < 0 or x >= width :
                return 
            if dp[y][x] == None :
                dp[y][x] = max(dfsHelper(x, y-1)if y-1 >= 0 and  matrix[y][x] > matrix[y-1][x] else 0,\
                               dfsHelper(x, y+1) if y+1 <height and matrix[y][x] > matrix[y+1][x] else 0,\
                               dfsHelper(x-1, y) if x-1 >= 0 and matrix[y][x] > matrix[y][x-1] else 0,\
                               dfsHelper(x+1, y) if x+1 <width and matrix[y][x] > matrix[y][x+1] else 0) + 1
            return dp[y][x]
        if not matrix: return 0
        height = len(matrix)
        width = len(matrix[0]) if matrix else 0
        dp = [[None]*width for _ in xrange(height)]
        return max(dfsHelper(x, y) for x in xrange(width) for y in xrange(height))


#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])


