class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower == upper:
                return [str(lower)]
            return [str(lower)+"->"+str(upper)]
        result = []
        nums.insert(0, lower-1)
        nums.append(upper+1)
        for i, num in enumerate(nums[1:], 1):
            if nums[i] - nums[i-1] >= 2:
                if nums[i] - nums[i-1] == 2:
                    result.append(str(num-1))
                else:
                    result.append(str(nums[i-1]+1)+"->"+str(nums[i]-1))
        return result


        # finalResult = []
        # start = lower
        # while result:
        #     currentStart, currentEnd = result.pop(0)

        #     finalResult.append((start, currentStart-1 ))
        #     start = currentEnd

        

#test:
if __name__ == "__main__":
    sol = Solution()
    arr = [0, 1, 3, 50, 75]
    print sol.findMissingRanges(arr, 0, 99)
