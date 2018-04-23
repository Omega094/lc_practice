class Solution(object):
    def getFactorsHelper(self, solutionList, currentNum, currentList):
        print currentList
        if currentNum == 1 and len(currentList) != 1:
            solutionList.append(currentList)
            return
        if currentList != [] : start = currentList[-1] 
        else :
            start = 2
        print currentNum, currentList, start
        for i in range(start, int(currentNum**0.5)+1):
            if currentNum % i == 0:
                self.getFactorsHelper(solutionList, currentNum/i, currentList[:]+[i])
        #Must Need 
        self.getFactorsHelper(solutionList, 1, currentList+[currentNum])
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        solutionList = []
        currentNum = n
        currentList = []
        self.getFactorsHelper(solutionList, currentNum, currentList)
        return solutionList


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.getFactors(12)
        
         
