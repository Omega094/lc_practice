class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        result = 0
        for c in s[::-1]:
            result = result + (ord(c)-64)*26**counter
            counter+=1
        return result
