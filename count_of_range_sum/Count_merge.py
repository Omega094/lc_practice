class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        def mergeHelper( low, high):
            mid = (low + high) / 2
            if mid == low : return 0
            count = mergeHelper( low, mid) + mergeHelper( mid, high)
            i = j = mid 
            for left in prefix[low:mid]:
                while i < high and prefix[i] - left <lower : i += 1
                while j < high and prefix[j] - left <= upper : j += 1
                count += j - i
            prefix[low:high] = sorted(prefix[low:high])
            return count 
        print prefix
        return mergeHelper( 0, len(prefix))
