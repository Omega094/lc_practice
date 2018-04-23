class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) == len(t):
            count = 0
            for i in xrange(len(s)):
                if s[i] != t[i]: count += 1
            return count == 1
        if abs(len(s) - len(t)) == 1:
            if len(s) < len(t):
                s, t = t, s
            i = 0
            while i < len(t) and s[i] == t[i]:
                i += 1
            i += 1
            count = 0
            while i < len(s):
                if s[i] != t[i-1]:
                    count += 1
                i += 1
            return count == 0
        return False
                
            
