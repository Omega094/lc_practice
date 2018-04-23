class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        return sum( i%2 for i in Counter(s).values()) < 2
    
    def palindromesBuilder(self, currentPalindrome, currentCounter, targetLen, solutionList):
        if len(currentPalindrome) == targetLen:
            solutionList.add(currentPalindrome)
            return 
        for c in currentCounter:
            if currentCounter[c] == 0: continue
            if currentCounter[c] == 1:
                currentCounter[c] -= 1
                newPal = currentPalindrome[0:len(currentPalindrome)/2] + c + currentPalindrome[len(currentPalindrome)/2:]
                self.palindromesBuilder(newPal,currentCounter, targetLen, solutionList)
                currentCounter[c] += 1
            else:
                currentCounter[c] -= 2
                newPal = c+currentPalindrome+c
                self.palindromesBuilder(newPal,currentCounter, targetLen, solutionList)
                currentCounter[c] += 2
                
    
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not self.canPermutePalindrome(s) or s == "": return []
        targetLen = len(s)
        currentPalindrone = ""
        solutionList = set()
        from collections import Counter
        currentCounter = Counter(s)
        self.palindromesBuilder(currentPalindrone, currentCounter, targetLen, solutionList)
        return list(solutionList)
        
        
        
#test
if __name__ == "__main__":
    sol = Solution()
    print sol.generatePalindromes("aabb")



