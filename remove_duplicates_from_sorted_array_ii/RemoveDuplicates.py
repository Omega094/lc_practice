class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentNum = nums[0]
        counter = 1
        isMoreThanOne = False
        for i, num in enumerate(nums[1:], 1):
            if num == nums[i-1]:
                if isMoreThanOne: continue
                isMoreThanOne = True
                counter += 1
            if nums[i] != nums[i-1] :
                counter += 1
                isMoreThanOne = False
        return counter

    def removeDuplicates_array(self, nums):
        if len(nums) <= 2:
            return len(nums)
        prev = 1
        curr = 2
        while (curr < len(nums)):
            if nums[curr] == nums[prev] and nums[curr] == nums[curr-1]:
                curr += 1
            else:
                prev += 1
                nums[prev] = nums[curr]
                curr += 1
        print nums
        return prev + 1

#test:
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    sol = Solution()
    #print sol.removeDuplicates(nums) 
    print sol.removeDuplicates_array(nums)
