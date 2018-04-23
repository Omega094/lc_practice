class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import Counter
        backPtr = 0
        ctr = Counter()
        maxLen = float("-inf")
        for i , c in enumerate(s):
            ctr[c] += 1
            while len(ctr) > k:
                ctr[s[backPtr]] -= 1
                if ctr[s[backPtr]] == 0:
                    del ctr[s[backPtr]] 
                backPtr += 1
            maxLen = max(maxLen, i - backPtr + 1)
        return maxLen if k != 0 and s != "" else 0

#test
sol = Solution()
print sol.lengthOfLongestSubstringKDistinct("eceba", 2)
