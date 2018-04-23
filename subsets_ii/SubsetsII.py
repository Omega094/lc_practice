class Solution(object):
    def subsetsWithDup(self, nums):
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
                if i >= 1 and numsList[i] == numsList[i-1]: continue
                self.subsetHelper(k, numsList[i+1:], currentList + [num], solutionList)
        return

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.subsetsWithDup([1,2,2])
