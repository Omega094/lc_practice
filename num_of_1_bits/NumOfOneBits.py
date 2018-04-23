class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        for i in xrange(32):
            counter += n & 1
            n = n >> 1
        return counter
