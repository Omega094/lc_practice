class Solution(object):
    def reverse(self, x):
        is_neg = False
        if x < 0:
            is_neg = True 
            x = -x
        result = 0
        while x != 0:
            result = 10*result + x%10
            x = int( x / 10 )
        if result > 2147483647: return 0
        if is_neg:
            result = result * -1
        return result

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.reverse(-123)


