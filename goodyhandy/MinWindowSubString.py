class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        missing = len(t)
        needed = Counter(t)
        i = left = right = 0
        for j, c in enumerate(s, 1):
            missing -= needed[c] > 0
            needed[c] -= 1
            if not missing:
                while needed[s[i]]< 0 and i < j :
                    needed[s[i]] += 1
                    i += 1
                if not right or (j - i) < (right - left):
                    right , left = j, i
        return s[left:right]
