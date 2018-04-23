class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        currentResult = ""
        while n != 0:
            currentDigit = n % 26
            if currentDigit == 0:
                currentDigit = 26
            currentResult = chr(64+currentDigit) + currentResult
            n =( n- currentDigit)// 26
        return currentResult

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.convertToTitle(100)
    print sol.convertToTitle(1)
    print sol.convertToTitle(2)
