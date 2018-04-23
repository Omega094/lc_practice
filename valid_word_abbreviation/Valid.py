class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        lWord = list(word)
        lAbbr = list(abbr)
        newList = []
        currentNum = ""
        while lAbbr:
            if not lAbbr[0].isdigit():
                if currentNum :
                    if currentNum[0] == "0": return False
                    newList.append(currentNum)
                    currentNum = ""
                newList.append(lAbbr.pop(0))
            else:
                currentNum += lAbbr.pop(0)
        if currentNum != "":
            if currentNum[0] == "0" : return False
            newList.append(currentNum)
        lAbbr = newList
        while lAbbr:
            if not lAbbr[-1].isdigit():
                if not lAbbr or not lWord or not (lAbbr.pop() == lWord.pop()): return False
            else:
                charNum = int(lAbbr.pop())
                if len(lWord) < charNum: return False
                lWord = lWord[:-charNum]
        return not lWord
            

#test
sol = Solution()
print sol.validWordAbbreviation("internationalization",  "i12iz4n")
print sol.validWordAbbreviation("apple", "a2e")
