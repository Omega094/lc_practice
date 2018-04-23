class Solution(object):
    def singleNumberGenericK(self, nums, k):
        res = 0
        for i in range(32):
            count = 0
            for n in nums:
                count += (n >> i) & 1
            rem = count % k
            if i == 31 and rem:  # must handle the negative case
                res -= 1 << 31
            else:
                res |= rem << i
        return res
        
    def singleNumber(self,nums):
        return self.singleNumberGenericK(nums, 3)
