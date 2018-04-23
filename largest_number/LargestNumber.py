class Solution(object):
    def largestNumber(self, nums):
        nums = sorted(nums, cmp = lambda x, y: cmp(str(y) + str(x) , str(x) + str(y)))
        result = ''
        for x in nums:
            result += str(x)
        return result.lstrip('0') or '0'

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.largestNumber([3, 30, 34, 5, 9])
