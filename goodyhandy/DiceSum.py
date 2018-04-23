class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        table = [[0 for _ in xrange(6*n + 1)] for j in xrange(n+1)]
        result = []
        for i in xrange(1, 7):
            table[1][i] = float(1)/6
        for i in xrange(2, n+1):
            for j in xrange(i,6*n+1):
                for k in xrange(1, 7):
                    if j > k :
                        table[i][j] += table[i-1][j-k]/6
        #print table
        for i in xrange(n, 6*n+1):
            result.append((i, table[n][i]))
        return result


#test
sol = Solution()
print sol.dicesSum(3)


        
