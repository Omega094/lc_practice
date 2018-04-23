class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
 
        sL = list(s)
        tL = list(t)
        while sL and tL:
            #if not sL: return True
            while tL[-1] != sL[-1]:
                tL.pop()
                if not tL: return False
            tL.pop(); sL.pop()
        if not sL:
            return True 
        return False
        
        
