class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        step = 1
        left = 1
        while n > 1:
            if left or n%2 == 1:
                start += step
            step *= 2
            n /= 2
            left = left ^ 1
        return start

#test
sol = Solution()
print sol.lastRemaining(9)
        
