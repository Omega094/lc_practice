class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for idx, num in enumerate(nums):
            if (target - num) in map:
                return [map[target - num], idx]
            map[num] = idx
        return []

#test:
if __name__ == "__main__":
    nums = [2,3,4]
    target = 6
    sol = Solution()
    print sol.twoSum(nums, target);
