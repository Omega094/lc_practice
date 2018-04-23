def kSum(A, k, tar):
    if tar == 0:
        return 0
    length = len(A)
    dp = [ [[0 for t in xrange(0, tar+1)] for j in xrange(0, k+1) ] for i in xrange(0, length+1)]
    for i in xrange(0, length +1):
        for j in xrange(0, k + 1):
            for t in xrange(0, tar+1):
                if j == 0 or t == 0:
                    dp[i][j][t] = 1
                elif not(i==0 or j == 0 or t==0):
                    dp[i][j][t] = dp[i-1][j][t]
                    if tar  - A[i-1] >= 0:
                        dp[i][j][t] += dp[i-1][j-1][t-A[i]]
    return dp[-1][-1][-1]
