class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = 0
        nums.sort()
        for i, num in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            currentTarget = target - num
            while j < k :
                if nums[j] + nums[k] < currentTarget:
                    total += k - j
                    j += 1
                else:
                    k -= 1
        return total

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.threeSumSmaller([-2, 0, 1, 3], 2)
