class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import Counter
        ctr = Counter()
        start = 0; maxFreq = 0; maxLen = 0
        for i, c in enumerate(s):
            ctr[c] +=  1; maxFreq = max(ctr.values())
            if i - start + 1 - maxFreq <= k:
                maxLen = max(maxLen, i - start + 1)
            while i - start + 1 - max(ctr.values()) > k:
                ctr[s[start]] -= 1
                start += 1
        return maxLen
        
