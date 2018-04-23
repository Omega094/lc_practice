class Solution(object):

    def permute(self, nums):
        if not nums: return [[]]
        if len(nums) == 1: return [nums]
        currentIndex = 0
        nums.sort()
        solutionList = []
        while currentIndex < len(nums):
            tempList = nums[:]
            tempList.remove(nums[currentIndex])
            lsts = self.permute(tempList)
            for lst in lsts:
                lst.append(nums[currentIndex])
                solutionList.append(lst)
            currentIndex += 1
            while currentIndex < len(nums) and nums[currentIndex] ==  nums[currentIndex-1]:
                currentIndex+= 1
        return solutionList

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.permute([1,1,2])


