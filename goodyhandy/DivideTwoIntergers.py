class Solution(object):

    def divide(self, dividend, divisor):
        MAX_INT = 2**31-1
        MIN_INT = -2**31
        if divisor == 0 or dividend == MIN_INT and divisor == -1:
            return MAX_INT
        negative = (dividend * divisor) < 0
        bit = 1
        dividend, divisor = map(abs, (dividend, divisor))
        if divisor > dividend: return 0
        #bit is directly related to divisor. 
        while divisor < dividend:
            divisor <<= 1
            bit <<= 1
        result = 0
        while bit >= 1:
            if dividend - divisor >= 0:
                result += bit
                dividend -= divisor
            divisor >>= 1
            bit >>= 1
        return -result if negative else result


