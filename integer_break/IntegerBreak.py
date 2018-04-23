class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        if n == 2: return 1
        if n == 3: return 2
        if n % 3 == 0:
            return 3**(n/3)
        if n%3 == 1:
            return 3**(n//3-1)*4
        if n %3 == 2:
            return 3**(n//3)*2

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.integerBreak(7)
    print sol.integerBreak(11)
