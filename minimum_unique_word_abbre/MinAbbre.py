class Solution(object):

    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        lWord = list(word)
        lAbbr =  [t for t in  re.split('(\D)', abbr) if t]
        while lAbbr:
            if not lAbbr[-1].isdigit():
                if not lAbbr or not lWord or not (lAbbr.pop() == lWord.pop()): return False
            else:
                charNum = int(lAbbr.pop())
                if len(lWord) < charNum: return False
                lWord = lWord[:-charNum]
        return not lWord
        
    def dfsHelper(self, currentStr, remainStr):
        currentLen = len([t for t in  re.split('(\D)', currentStr) if t] )
        if self.currentMinLen and currentLen > self.currentMinLen: return 
        if remainStr == "":
            for w in self.dictionary: 
                if self.validWordAbbreviation(w, currentStr):
                    return 
            if self.currentMin == None or currentLen < len(self.currentMin) :
                self.currentMin = currentStr
                self.currentMinLen = currentLen
            return
        if len(currentStr) == 0 or currentStr[-1].isdigit():
            for i in range(1, len(remainStr)+1):
                self.dfsHelper( currentStr + remainStr[:i] , remainStr[i:])
        if len(currentStr) == 0 or not currentStr[-1].isdigit():
            for i in range(1, len(remainStr)+1):
                self.dfsHelper( currentStr + str(i) , remainStr[i:])
            return
    

        
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        self.dictionary = dictionary
        self.currentMin = None
        self.currentMinLen = None
        self.dfsHelper("", target)
        return self.currentMin
        
        
        
