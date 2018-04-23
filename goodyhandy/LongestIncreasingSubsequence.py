class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = []
        for i, num in enumerate(nums):
            start = 0
            end = len(table)- 1 
            mid = (start + end) // 2
            while start <= end:
                mid = (start + end) // 2
                if  table[mid] > num :
                    end = mid - 1
                else:
                    start = mid + 1
            if start >= len(table):
                table.append(num)
            else:
                table[start] = num
        return len(table)

#test
sol = Solution()
print sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
