class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self._data = [0 for i in xrange(len(nums))]
        for i in xrange(0, len(nums)):
            self._data[i] = (nums[i] + self._data[i-1]) if i > 0 else nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self._data: return 
        if i == 0:
            return self._data[j] 
        else:
            return self._data[j] - self._data[i-1]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
