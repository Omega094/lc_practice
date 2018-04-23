class Solution(object):
    
    def subsets(self, nums):
        solutionList = []
        nums.sort()
        for i in range (0, len(nums) + 1):
            self.subsetHelper(i, nums, [], solutionList)
        return solutionList

    def subsetHelper(self, k, numsList, currentList, solutionList):
        if len(currentList) == k:
            solutionList.append(currentList)
        else:
            for i, num in enumerate(numsList):
                self.subsetHelper(k, numsList[i+1:], currentList + [num], solutionList)
        return 

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.subsets([1,2,3])
