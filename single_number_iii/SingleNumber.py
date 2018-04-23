class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda x, y : x ^ y, nums)
        lowbit = xor & -xor
        result = [0, 0]
        for num in nums:
            result[ not (lowbit&num)] ^= num
        return result

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.singleNumber([1, 2, 1, 3, 2, 5])
