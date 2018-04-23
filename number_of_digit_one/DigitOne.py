class Solution(object):
    def countDigitOne(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n/m + 8) / 10 * m + (n/m % 10 == 1) * (n%m + 1)
            m *= 10
            print m
        return ones
    
    def countDigitOne_explicit(self, n):
        result = 0
        k = 1
        while k <= n:
            a = n/k
            b = n%k
            result += (a+8)/10 * k
            if (a%10 == 1):
                result += b+1
            k *= 10
        return result




if __name__ == "__main__":
    sol = Solution()
    print sol.countDigitOne(1301)
    print sol.countDigitOne_explicit(1301)
