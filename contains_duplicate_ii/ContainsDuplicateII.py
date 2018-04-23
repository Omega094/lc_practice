class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indexDict = {}
        for i, num in enumerate(nums):
            if num in indexDict and i - indexDict[num] <= k:
                    return True
            indexDict[num] = i
        return False

if __name__ == "__main__":
    sol = Solution()
    print sol.containsNearbyDuplicate([1,2,3,4,5,6,4], 3)

