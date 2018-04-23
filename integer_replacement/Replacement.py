class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {1:0}
        return self.recRep(n, memo)
        
    def recRep(self, n, memo):
        if n in memo:
            return memo[n]
        if n % 2:
            memo[n] = 1 + min(self.recRep(n+1, memo), self.recRep(n-1, memo))
            return memo[n]
        else:
            memo[n] = 1 + self.recRep(n/2, memo)
            return memo[n]
