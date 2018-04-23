class Solution(object):
    
    def dfs(self, remainP,remainStr, pToW, valueSet):
        if remainStr == "" and remainP == "":
            return True
        if remainP == "" or remainStr == "": return False
        for i in range(1, len(remainStr)+1):
            w = remainStr[:i]
            p = remainP[0]
            if p in pToW and pToW[p] != w: continue
            if p not in pToW :
                if w in valueSet: continue
                pToW[p] = w
                valueSet.add(w)
                if self.dfs(remainP[1:], remainStr[i:], pToW, valueSet) : return True
                del pToW[p]
                valueSet.remove(w)
            else:# pToW[p] == w:
                if self.dfs(remainP[1:], remainStr[i:], pToW, valueSet) : return True
        return False
            
    def wordPatternMatch(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # if not pattern : return str == ""
        # if not str: return pattern == ""
        from collections import defaultdict
        pToW = defaultdict(str)
        return self.dfs(pattern, s, pToW, set())
        
        
        
        
