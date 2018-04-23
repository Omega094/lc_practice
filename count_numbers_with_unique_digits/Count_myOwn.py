class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        if n == 1: return 10
        if n == 2: return 91
        import math
        if n > 10:
            return self.countNumbersWithUniqueDigits(10)
        current = 9
        for i in range(9,9-n+1, -1):
            current*=i
        return current  + self.countNumbersWithUniqueDigits(n-1)
        
