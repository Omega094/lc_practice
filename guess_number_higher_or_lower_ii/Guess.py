class Solution(object):
 
    def getMoneyAmount(self, n):
        need = [[0] * (n+1) for _ in range(n+1)]
        for lo in xrange(n, 0, -1):
            for hi in xrange(lo+1, n+1):
                need[lo][hi] = min(i + max(need[lo][i-1]  , need[i+1][hi]) for i in xrange(lo, hi))
        for row in need:
            print row
        return need[1][n]

sol = Solution()
print sol.getMoneyAmount(10)
