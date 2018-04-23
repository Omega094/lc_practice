class Solution(object):
    
    def memoSearch(self, n ):
        if n in self.memo:
            return self.memo[n]
        if n % 2 == 0:
            result = 1 + self.memoSearch(n/2)
        else:
            result = 1 + min(self.memoSearch(n+1), self.memoSearch(n-1))
        self.memo[n] = result
        return result 
        
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = {1:0}
        return self.memoSearch(n)
