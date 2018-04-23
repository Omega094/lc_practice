class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
 
    def kSum(self, A, k, target):
        ans = [[[0 for i in range(target + 1)] for j in range(k + 1)] for K in range(len(A) + 1)]
        for i in xrange(0, len(A) + 1): ans[i][0][0] = 1
 
        for i in xrange(1, len(A)+1):
            for j in xrange(1, k+1):
                if j > i: break
                for t in xrange(1, target + 1):
                    ans[i][j][t] = ans[i-1][j][t]
                    if A[i-1] <= t:
                        ans[i][j][t] += ans[i-1][j-1][t-A[i-1]]
        return ans[len(A)][k][target]
