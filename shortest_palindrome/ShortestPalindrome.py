class Solution(object):
    def shortestPalindrome(self, s):
        reversedS = s[::-1]
        newStr = s + "#" + reversedS
        lengthTable = [0]*len(newStr)
        for i in range(1, len(newStr)):
            j = lengthTable[i-1]
            while j > 0 and newStr[i] != newStr[j]:
                j = lengthTable[j-1]
            lengthTable[i] = j + (newStr[i] == newStr[j])
        return reversedS[:len(s) - lengthTable[-1]] + s


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.shortestPalindrome("ab")
    print sol.shortestPalindrome("abc")
    print sol.shortestPalindrome("abcd")
