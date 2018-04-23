class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        positionDict = {}
        backPtr = 0
        maxLen = 0
        for i , c in enumerate(s):
            #The second scenario in case below is most important.
            if c not in positionDict or positionDict[c] < backPtr:
                maxLen = max(maxLen, i - backPtr + 1)
            else:
                maxLen = max(maxLen, i - backPtr)
                backPtr = positionDict[c] + 1
            positionDict[c] = i
        return maxLen

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.lengthOfLongestSubstring("abcabcbb")
    print sol.lengthOfLongestSubstring("pwwkew") 
