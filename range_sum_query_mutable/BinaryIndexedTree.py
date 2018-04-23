class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums = nums
        self.ft = [0] * (self.n+1)
        for i, num in enumerate(nums):
            k = i + 1
            while k <= self.n:
                self.ft[k] += num
                k += (k & -k)
        return 

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        i = i + 1
        while i <= self.n:
            self.ft[i] += diff
            i += (i & -i)
        return 

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
     
        j = j + 1
        sumi = 0
        while i > 0:
            sumi += self.ft[i]
            i -= (i & -i)
        sumj = 0
        while j > 0:
            sumj += self.ft[j]
            j -= (j & -j)
        return sumj - sumi
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
