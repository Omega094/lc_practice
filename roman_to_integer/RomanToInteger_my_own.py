class Solution(object):
    #The rule is that each roman decreases from left to right 
    #And double letter 's left roman is less than its right roman
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        valDict = {}
        for i in range(0, len(numerals)):
            valDict[numerals[i]] = values[i]
        result = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and valDict[s[i+1]] > valDict[s[i]]:
                currentRoman = s[i:i+2]
                i += 2
            else:
                currentRoman = s[i:i+1]
                i += 1
            result += valDict[currentRoman]
        return result 
