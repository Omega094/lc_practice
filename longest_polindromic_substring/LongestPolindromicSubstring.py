import sys
sys.path.append("/Users/jinzhao/leetcode/")
class Solution(object):
    def getLongestPolindrom(self, s, l, r):
        while l >=0 and r < len(s) and s[l] == s[r]:
            l-= 1; r += 1
        return s[l+1: r ]
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxPolindrom = "";
        for i, c in enumerate (s , 0):
            p1 = self.getLongestPolindrom(s, i, i)
            p2 = self.getLongestPolindrom(s, i, i+1)
            if len(p1) < len(p2):
                p1 = p2
            if len(p1) > len(maxPolindrom):
                maxPolindrom = p1
        return maxPolindrom

#test 
if __name__ == "__main__" :
    sol = Solution()
    print sol.longestPalindrome("fskaljfaaaaabaaaaafskjjhfkhfs")

