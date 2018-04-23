class Solution(object):
    def moveZeroes(self, nums):
        cur = 0
        for i in range(0, len(nums)):
            if nums[i]:
                nums[cur] = nums[i]
                cur += 1
        for j in range(cur, len(nums)):
            nums[j] = 0
        return nums

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.moveZeroes([0, 1, 0, 3, 12])
