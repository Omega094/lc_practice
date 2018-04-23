class Solution(object):

    def countAndSay(self, n):
       intStr = '1'
        result = '1'
        for i in range (1, n):
            intStr = result 
            result = ''
            currentCounter = 0
            currentChar = intStr[0]
            for i in range (0, len(intStr)):
                if intStr[i] == currentChar:
                    currentCounter += 1
                else:
                    result += (str(currentCounter)+currentChar)
                    currentCounter = 1
                    currentChar = intStr[i]
            result += (str(currentCounter)+currentChar)
        return result





#test
if __name__ == "__main__":
    sol = Solution()
    print sol.countAndSay(6)
