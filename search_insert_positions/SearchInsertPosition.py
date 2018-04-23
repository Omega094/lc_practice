class Solution(object):

    def searchInsert(self, nums, target):
        if not nums: return 0
        start = 0
        end = len(nums) - 1
        found = False
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                found = True
                break
            if start == end: break
            if nums[mid] > target:
                end = mid
            else:
                start = mid + 1
        if found: return mid
        if nums[mid] < target: return mid + 1
        return mid


#test:
if __name__ == "__main__":
    nums = [1,3,5,6]
    sol = Solution()
    print sol.searchInsert(nums, 5)
    print sol.searchInsert(nums, 2)
    print sol.searchInsert(nums, 7)
    print sol.searchInsert(nums, 0)

