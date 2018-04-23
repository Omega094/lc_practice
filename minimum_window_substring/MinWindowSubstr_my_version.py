class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        missing = len(t)
        ctr = Counter(t)
        i = left = right = 0
        for j, c in enumerate(s, 1):
            if c in ctr:
                if ctr[c] > 0:
                    missing -= 1
                ctr[c] -= 1
            if not missing:
                while (s[i] not in ctr or ctr[s[i]] < 0) and i < j:
                    if s[i] in ctr:
                        ctr[s[i]] += 1
                    i += 1
                if not right or(j - i) < (right - left):
                    right, left = j, i
        return s[left: right]
        
