class Solution(object):
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        result = ""
        for i in range (0, len(values)):
            while num >= values[i]:
                result += numerals[i]
                num -= values[i]
        return result


#test 
if __name__ == "__main__":
    sol = Solution()
    print sol.intToRoman(12345)

