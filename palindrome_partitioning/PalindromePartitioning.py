class Solution(object):
    
    def isPalindrome(self, a):
        return a == a[::-1]
    
    def dfsHelper(self, strRest, currentSolution, solutionList):
        if strRest == "":
            solutionList.append(currentSolution)
        for i in range(0, len(strRest)):
            if self.isPalindrome(strRest[:i+1]):
                self.dfsHelper(strRest[i+1:], currentSolution+[strRest[:i+1]], solutionList)
        return 
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        solutionList = []
        self.dfsHelper(s, [], solutionList)
        return solutionList


#test
if __name__ == "__main__":
    sol = Solution()
    s = "aab"
    print sol.partition(s)
