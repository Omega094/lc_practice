class Solution(object):
    def getFactorsHelper(self, solutionList, currentNum, currentList):
        if currentNum == 1 and len(currentList) > 1:
            solutionList.append(currentList)
            return
        if currentList: start = currentList[-1] 
        else :
            start = 2
        for i in xrange(start, currentNum+1):
            #print currentNum, "Currne"
            if currentNum % i == 0:
                self.getFactorsHelper(solutionList, currentNum/i, currentList[:]+[i])
            #print currentList
        return 

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1: return []
        solutionList = []
        currentNum = n
        currentList = []
        self.getFactorsHelper(solutionList, currentNum, currentList)
        return solutionList
