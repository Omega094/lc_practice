class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in xrange(32):
            result = result << 1
            thisBit = 1 & n
            result |= thisBit
            n = n >> 1
        return result 


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.reverseBits(43261596)
