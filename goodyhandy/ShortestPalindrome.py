class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversedS = s[::-1]
        newStr = s + "#" + reversedS
        lengthTable = [0]*len(newStr)
        for i in range(1, len(newStr)):
            j = lengthTable[i-1]
            while j > 0 and newStr[i] != newStr[j]:
                j = lengthTable[j-1]
            lengthTable[i] = j + (newStr[i] == newStr[j])
        return reversedS[:len(s) - lengthTable[-1]] + s
        
        
