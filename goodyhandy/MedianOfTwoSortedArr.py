class Solution(object):
    
    def getKth(self, a1, a2, k):
        if len(a1) > len(a2): 
            a1, a2 = a2, a1
        if len(a1) == 0:
            return a2[k-1]
        if k == 1:
            return min(a1[0], a2[0])
        p1 = min(k/2, len(a1))
        p2 = k - p1
        if a1[p1-1] < a2[p2-1]:
            return self.getKth(a1[p1:], a2, p2)
        else:
            return self.getKth(a1, a2[p2:], p1)
    
        
    
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenA = len(A); lenB = len(B)
        if (lenA + lenB) % 2 == 1: 
            return self.getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5
        
