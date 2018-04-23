class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s): return ""
        if len(t) == len(s):
            if sorted(list(s)) == sorted(list(t)): return s
            return ""
        need = len(t)
        from collections import Counter
        ctr = Counter(t)
        i, j = 0, 0
        backPtr = 0
        for frontPtr in xrange(0, len(s)):
            if s[frontPtr] in ctr:
                if ctr[s[frontPtr]] > 0 :
                    need -= 1
                ctr[s[frontPtr]] -= 1
            if need == 0:
                while frontPtr > backPtr and (s[backPtr] not in ctr or (ctr[s[backPtr]] < 0 )):
                     
                    #print backPtr, "backPtr"
                    if s[backPtr] in ctr: ctr[s[backPtr]] += 1
                    backPtr += 1
                    if j == 0 or frontPtr - backPtr + 1 < j - i + 1:
                        j, i = frontPtr, backPtr
                 
        return s[i:j+1]
        
