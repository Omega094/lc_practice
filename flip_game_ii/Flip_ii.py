class Solution(object):
    
    def helper(self, s):
        if s in self.cache : return self.cache[s]
        if s.count("++") == 1: 
            self.cache[s] = True
            return True
        if s.count("++") == 0: 
            self.cache[s] = False
            return False
        for i in xrange(0, len(s) - 1):
            if s[i:i+2] == "++" and self.helper(s[:i] + "--" +s[i+2:]) == False:
                self.cache[s] = True
                return True
        self.cache[s] = False
        return False
        
    
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.cache = {}
        return self.helper(s)
        
        
