class Solution(object):
    def permute(self, nums):
        solutionList = []
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums]
        #recursion
        for i, num in enumerate (nums):
            tempList = nums[:]
            tempList.remove(num)
            permutations = self.permute(tempList)
            for lst in permutations:
                lst.append(num)
                solutionList.append(lst)
        return solutionList

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.permute([1,2,3])
    print sol.permute([1,2,3,4,5,6])
