class Solution(object):

    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
             return 1
        else:
            lst = [[0 for i in xrange(n)] for j in xrange(m)]
            for i in xrange(n): lst[0][i] = 1
            for j in xrange(m): lst[j][0] = 1
            for i in range(1, m):
                for j in range(1, n):
                    lst[i][j] = lst[i-1][j] + lst[i][j-1]
            return lst[m-1][n-1]

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.uniquePaths(3,7)
