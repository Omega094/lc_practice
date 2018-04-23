class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        ctr = Counter(s)
        totalLen = 0
        vals = ctr.values()
        maxOdd = None
        for v in vals:
            if v %2 == 0:
                totalLen += v
            else:
                totalLen += max(v-1, 0)
                maxOdd = max(maxOdd, v)
        if maxOdd: totalLen += 1 
        return totalLen
#test
sol = Solution()
print sol.longestPalindrome("abccccdd")
        
