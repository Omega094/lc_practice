class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k**2
        paintTable = [0] * n
        paintTable[0] = k
        paintTable[1] = k**2
        for i in range(2, n):
            paintTable[i] = (k-1)*(paintTable[i-1]+paintTable[i-2])
        return paintTable[-1]

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.numWays(4, 4)
    print sol.numWays(5,4)
