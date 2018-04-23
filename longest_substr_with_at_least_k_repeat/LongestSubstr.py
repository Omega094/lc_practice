from collections import Counter
class Solution(object):
 
    def longestSubstring(self, s, k):
        if len(s) < k: return 0
        ctr = Counter(s)
        if min(ctr.values()) >= k:
            return len(s)
        idx = []
        for i in xrange(len(s)):
            if ctr[s[i]] < k:
                s = s[:i] + "#" + s[i+1:]
        subStrs = s.split("#")
        currentMax = max(map(lambda x : self.longestSubstring(x,k), subStrs))
        return currentMax
        

#test
s = "ababbc"; k = 2
sol = Solution()
print sol.longestSubstring(s, k)
