class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 2147483648%n == 0
   
    def isPowerOfTwo_2(self, n):
        if n == 0 or n < 0 : return False
        while n != 1:
            if not(n & 1) == 0: return False
            n >>= 1
        return True
