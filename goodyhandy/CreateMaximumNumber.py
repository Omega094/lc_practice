class Solution(object):
    def maxKFromArr(self, nums, k):
        res = []; n = len(nums)
        for i, num in enumerate(nums):
            while res and num > res[-1] and len(res) + n - i > k:
                res.pop()
            if len(res) < k:
                res.append(num)
        return res
            
            
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        ans = [0]*k
        m, n = len(nums1), len(nums2)
        for i in xrange(0, k+1):
            j = k - i
            if i > m or j > n: continue
            left  = self.maxKFromArr(nums1, i)
            right = self.maxKFromArr(nums2, j)
            #print left, right
            ans = max(ans, [max(left,right).pop(0) for x in xrange(k)])
        return ans

#test
sol = Solution()
print sol.maxKFromArr([9, 1, 2, 5, 8, 3], 8)
        
