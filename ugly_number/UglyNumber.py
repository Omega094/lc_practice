class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0: return False
        while num != 1:
            if not any([ num % 2 == 0 , num%3 == 0 , num%5 == 0]):
                return False
            else:
                if num % 2 == 0:
                    num /= 2
                elif num %3 == 0:
                    num /= 3
                else:
                    num/= 5
        return True

if __name__ == "__main__":
    sol = Solution()
    print sol.isUgly(14)
    print sol.isUgly(30)
