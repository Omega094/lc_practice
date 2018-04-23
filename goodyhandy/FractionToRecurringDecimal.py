class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        n = numerator; d = denominator
        res = ''
        if n%d == 0: return str(n//d)
        if n * d < 0 : res += '-'
        n , d = map(abs, (n, d))
        res += str(n//d) + '.'
        n %= d
        i = len(res)
        table = dict()
        while n != 0:
            if n not in table:
                table[n] = i
            else:
                i = table[n]
                res = res[:i] + '(' + res[i:] + ')'
                return res
            n*= 10
            res += str(n // d)
            n %= d
            i += 1
        return res

sol = Solution()
print sol.fractionToDecimal(2, 3)

