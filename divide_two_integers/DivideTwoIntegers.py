class Solution(object):
    
    def getA(self, x):
        bit = 1
        A = []
        while bit < x:
            bit <<= 1
        while bit:
            a = bit <= x
            A.append(a)
            x -= a*bit 
            bit >>= 1
        return A


    def divide(self, dividend, divisor):
        MAX_INT = 2**31-1
        MIN_INT = -2**31
        if divisor == 0 or dividend == MIN_INT and divisor == -1:
            return MAX_INT
        negative = (dividend < 0) != (divisor < 0)
        bit = 1
        dividend, divisor = map(abs, (dividend, divisor))
        if divisor > dividend: return 0
        while divisor < dividend:
            divisor <<= 1
            bit <<= 1
        result = 0
        while bit >= 1:
            if dividend - divisor >= 0:
                dividend -= divisor
                result += bit
            divisor >>= 1
            bit >>= 1
        return -result if negative else result

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.getA(99)
    print sol.divide(16, 2)
    print sol.divide(1,-1)
    print sol.divide(0, 1)
    print sol.divide(500, 5)
    print sol.divide(500,3)
