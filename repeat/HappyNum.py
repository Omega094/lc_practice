class Solution(object):
    def isHappy(self, n):
        s = set()
        while n != 1:
            if n in s :
                return False
            s.add(n)
            result = 0
            while n != 0:
                result = result + (n%10) ** 2
                n = n / 10
            n = result 
        return True
#test
if __name__ == "__main__":
    sol = Solution()
    print sol.isHappy(19)
                
