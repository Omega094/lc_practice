class Solution(object):

    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2:
            return self.myPow(x*x, n/2)*x
        return self.myPow(x*x, n/2)

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.myPow(2,-2)
    print sol.myPow(2,4)
