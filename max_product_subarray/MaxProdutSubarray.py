class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minTemp = nums[0]
        maxTemp = nums[0]
        maxProduct = nums[0]
        for num in nums[1:]:
            a = num*maxTemp
            b = num*minTemp
            c = num
            maxTemp = max(max(a, b), num)
            minTemp = min(min(a, b), num)
            maxProduct = max(maxProduct, maxTemp)
        return maxProduct


#test:
if __name__ == "__main__":
    sol = Solution()
    arr = [2,3,-2,4]
    print sol.maxProduct(arr)

