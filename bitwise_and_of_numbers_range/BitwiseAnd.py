class Solution(object):
    #The result is the common left header of m and n
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        counter = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            counter += 1
        m = m << counter
        return m
