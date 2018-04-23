class Solution(object):
    
    def check(self, s, wordDict):
        table = [ False for _ in xrange(len(s))]
        for i in xrange(len(s)):
            if s[:i+1] in wordDict:
                table[i] = True
                continue 
            for j in xrange(i, 0, -1):
                if s[j:i+1] in wordDict and table[j-1] == True:
                    table[i] = True
                    break
        return table[-1]
    
    def searchHelper(self, solution, currentList, currentStr,  wordDict):
        if currentStr == "": 
            solution.append(currentList)
            return
        if not self.check(currentStr, wordDict): return 
        for i in xrange(1, len(currentStr) +1 ):
            if currentStr[:i] in wordDict and (currentStr[i:] == "" or self.check(currentStr[i:], wordDict) ):
                self.searchHelper(solution, currentList + " " + currentStr[:i], currentStr[i:], wordDict)
        return
        
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        solution = []
        currentList = ""
        self.searchHelper(solution, currentList, s, wordDict)
        return map(lambda x : x.strip(), solution)
