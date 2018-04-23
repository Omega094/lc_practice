class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = m + n
        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[index-1] = nums1[m-1]
                m -= 1
            else:
                nums1[index-1] = nums2[n-1]
                n -= 1
            index -= 1
        #If n is exhausted, then we have nums1 part already sorted. 
        while n:
            nums1[index - 1] = nums2[n-1]
            n -= 1
            index -= 1

