class Solution(object):
    def longestPalindrone(self, s , start, end):
        while start >=0 and end < len(s) and s[start] == s[end]:
            start-=1
            end += 1
        return s[start+1:end]
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        for i in xrange(len(s)):
            p1 = self.longestPalindrone(s, i, i)
            p2 = self.longestPalindrone(s, i, i+1)
            if len(p1) > len(p2):
                p = p1
            else:
                p = p2
            if len(p) > len(longest):
                longest = p
        return longest
        
