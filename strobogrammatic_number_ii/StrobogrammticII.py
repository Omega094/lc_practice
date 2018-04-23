class Solution(object):
    
    def dfsHelper(self, n, currentStr, pairDict, solutionList):
        if n == 0:
            solutionList.append(currentStr)
            return
        length = len(currentStr)
        left = currentStr[:length/2]
        right = currentStr[length/2:]
        if n == 1:
            for c in ["1","8","0"]:
                self.dfsHelper(0, left+c+right, pairDict, solutionList)
            return 
        for leftC, rightC in pairDict.iteritems():
            self.dfsHelper(n-2, left+leftC+rightC+right, pairDict, solutionList)
        return
    
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pairDict = {"1": "1", "8": "8", "6": "9", "9":"6", "0":"0"}
        solutionList = []
        self.dfsHelper(n, "", pairDict, solutionList)
        return solutionList
        

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.findStrobogrammatic(19)
