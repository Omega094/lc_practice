class Solution(object):

    def combine(self, n, k):
        numList = [i for i in range (1, n+1)]
        solutionList = []
        currentList = []
        self.helper(currentList, numList, k, solutionList)
        return solutionList


    def helper(self, currentList, numList, k, solutionList):
        if len(currentList) == k:
            solutionList.append(currentList)
        else:
            for i , num in enumerate(numList):
                self.helper(currentList + [numList[i]], numList[i+1:], k, solutionList)
        return 


#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.combine(4, 2)
