class Solution(object):
    def generateHelper(self, current, left, right, solutionList):
        if left == 0 and right == 0:
            solutionList.append(current)
            return 
        if left<0 or right < 0 or  left > right: return 
        self.generateHelper(current+"(", left - 1, right, solutionList)
        self.generateHelper(current+")", left, right-1, solutionList)
        return 
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        solutionList = []
        self.generateHelper("", n, n, solutionList)
        return solutionList
        
        
