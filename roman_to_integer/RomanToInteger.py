class Solution(object):
    def RomanToInteger(self, roman):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        valDict = {}
        for i in range (0, len(numerals)):
            valDict[numerals[i]] = values[i]
        result = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and valDict[roman[i+1]] > valDict[roman[i]] :
                rom = roman[i:i+2]
                i += 2
            else:
                rom = roman[i]
                i += 1
            result += valDict[rom]
        return result 

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.RomanToInteger("MMMMMMMMMMMMCCCXLV")
