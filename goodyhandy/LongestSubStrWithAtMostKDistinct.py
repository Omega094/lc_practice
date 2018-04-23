class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0: return 0
        from collections import defaultdict
        positionTable = defaultdict(int)
        frontPtr = 0
        backPtr = 0
        maxLen = 0
        while frontPtr < len(s):
            positionTable[s[frontPtr]] +=1
            while len(positionTable) > k and backPtr < frontPtr:
                positionTable[s[backPtr]] -= 1
                if positionTable[s[backPtr]] == 0: del positionTable[s[backPtr]]
                backPtr += 1
            if frontPtr - backPtr + 1> maxLen:
                maxLen = frontPtr - backPtr + 1
            frontPtr += 1
        return maxLen
        
