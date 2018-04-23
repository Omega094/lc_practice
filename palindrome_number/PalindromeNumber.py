class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        result = 0
        copyX = x
        while copyX > 0:
            result = result*10 + copyX%10
            copyX = copyX/10
        return result == x

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.isPalindrome(1998888991)
    print sol.isPalindrome(-1998888991)
