class Solution(object):
    
    def dfs(self, remainP,remainStr, currentDictToWord):
        if remainStr == "" and remainP == "":
            return True
        if remainP == "" or remainStr == "": return False
        for i in range(1, len(remainStr)+1):
            word = remainStr[:i]
            s = remainP[0]
            if currentDictToWord.get(s, None) not in ( None, word): continue
            if currentDictToWord.get(s, None) == None:
                if word in currentDictToWord.values(): continue
                currentDictToWord[s] = word
                if self.dfs(remainP[1:], remainStr[i:], currentDictToWord): return True
                del currentDictToWord[s]
            else:
                if self.dfs(remainP[1:], remainStr[i:], currentDictToWord): return True
        return False
            
            
            
    
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # if not pattern : return str == ""
        # if not str: return pattern == ""
        return self.dfs(pattern, str, {})
