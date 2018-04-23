class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        currentCumulativeSum = 0
        left = 0
        minDist = float("inf")
        for i, num in enumerate(nums):
            currentCumulativeSum += num
            while currentCumulativeSum >= s:
                minDist = min(minDist, i - left + 1)
                currentCumulativeSum -= nums[left]
                left += 1
        return minDist if minDist != float("inf") else 0




#test:
if __name__ == "__main__":
    sol = Solution()
    testList = [2,3,1,2,4,3]
    print sol.minSubArrayLen(7,testList)
