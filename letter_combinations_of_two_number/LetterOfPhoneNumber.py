#Straight forward recursion DFS
#Time O(3**k)

class Solution(object):
    def letterCombinations(self, digits):
        if not digits: return []
        textDict = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        solutionList = []
        currentDigits = digits
        currentText = ""
        self.helper( textDict ,solutionList ,currentDigits, currentText)
        return solutionList

    def helper(self, textDict, solutionList ,currentDigits, currentText):
        if not currentDigits: 
            solutionList.append(currentText)
            return
        currentDigit = currentDigits[0]
        for c in textDict[currentDigit]:
            newText = currentText+c
            self.helper(textDict, solutionList, currentDigits[1:], newText)

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.letterCombinations("23")

