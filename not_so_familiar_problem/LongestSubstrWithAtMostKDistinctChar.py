#Just maintain two things 
#1: The back pointer
#2: The dictionary with length k 

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import Counter
        counter = Counter()
        maxLen = 0
        backPtr = 0
        for i, c in enumerate(s):
            counter[c] += 1
            while len(counter) > k:
                counter[s[backPtr]] -= 1
                if counter[s[backPtr]] == 0:
                    del counter[s[backPtr]]
                backPtr += 1
            maxLen = max(maxLen, i - backPtr + 1)
        return maxLen
    
#test
sol = Solution()
print sol.lengthOfLongestSubstringKDistinct("eceba", 2)
