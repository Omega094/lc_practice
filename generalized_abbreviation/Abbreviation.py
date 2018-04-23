class Solution(object):
    
    def dfsHelper(self, currentStr, remainStr, solutionList):
        if remainStr == "":
            solutionList.append(currentStr)
            return
        if len(currentStr) == 0 or currentStr[-1].isdigit():
            for i in range(1, len(remainStr)+1):
                self.dfsHelper( currentStr + remainStr[:i] , remainStr[i:], solutionList)
        if len(currentStr) == 0 or not currentStr[-1].isdigit():
            for i in range(1, len(remainStr)+1):
                self.dfsHelper( currentStr + str(i) , remainStr[i:], solutionList)
            return
    
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        solutionList = []
        self.dfsHelper("", word, solutionList)
        return solutionList

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.generateAbbreviations("word")
