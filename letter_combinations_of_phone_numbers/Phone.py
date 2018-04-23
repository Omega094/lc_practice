class Solution(object):
    
    def letterCombinations(self, digits):
        if not digits: return []
        textDict = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        solutionList = []
        currentDigits = digits
        currentText = ""
        self.dfsHelper(textDict, currentDigits, currentText, solutionList)
        return solutionList
    
    def dfsHelper(self, textDict, currentDigits, currentText, solutionList):
        if currentDigits == "":
            solutionList.append(currentText)
            return
        digit = currentDigits[0]
        for c in textDict[digit]:
            self.dfsHelper(textDict, currentDigits[1:], currentText + c, solutionList)
        return 
    
