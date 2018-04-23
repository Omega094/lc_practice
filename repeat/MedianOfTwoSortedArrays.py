class Solution(object):

    def getKth(self, A, B, k):
        lenA, lenB = len(A), len(B)
        if lenA > lenB: return self.getKth(B, A, k)
        if lenA == 0: return B[k-1]
        if k == 1: return min(A[0], B[0])
        #Now we start to partition. 
        pa = min(k/2, lenA)
        pb = k - pa
        #Keep excluding
        if A[pa-1] < B[pb-1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)

    def findMedianSortedArrays(self, A, B):
        lenA = len(A); lenB = len(B)
        if (lenA + lenB) % 2 == 1: 
            return self.getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5

#test:
if __name__ == "__main__":
   sol = Solution()
   A = [1,2,3,4,5]
   B = [3,4,5,6,7]
   print sol.findMedianSortedArrays(A, B)
