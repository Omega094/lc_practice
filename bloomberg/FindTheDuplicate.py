#O(nlogn) Solution
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 1
        end = len(nums)-1
        while start <= end:
            mid = (start + end) // 2 
            print start, end, mid,"Start, end, mid"
            pivot = mid
            smaller = 0
            for num in nums:
                if num <= pivot:
                    smaller += 1
            if smaller > pivot:
                end = mid - 1
            else:
                start = mid + 1
        return start
