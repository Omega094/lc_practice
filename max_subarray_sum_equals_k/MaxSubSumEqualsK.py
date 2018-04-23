#This problem is same throught as range sum query !
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        indexMap = {}
        sum = 0
        maxK = 0
        for i, num in enumerate(nums, 0):
            sum = sum + num
            if sum == k:
                maxK = i + 1
            elif sum - k in indexMap:
                maxK = max(maxK, i - indexMap[sum-k])
            if sum not in indexMap:
                indexMap[sum] = i
        return maxK



#test:
if __name__ == "__main__":
    lst = [1, 0, -1]
    k = -1
    sol = Solution()
    print sol.maxSubArrayLen(lst, k)
