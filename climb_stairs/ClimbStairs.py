class Solution(object):
    def climbStairs(self, n):
        first = 1
        second = 2
        if n == 1: return 1
        if n == 2: return 2
        for i in range (2, n):
            current = first + second
            first = second
            second = current
        return current



#test
if __name__ == "__main__":
    sol = Solution()
    print sol.climbStairs(5)

