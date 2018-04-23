class Solution(object):
    def firstMissingPositive(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(A)
        for i, num in enumerate(A):
            if A[i] != i + 1:
                while A[i] != i + 1:
                    if A[i] <= 0 or A[i] > length or A[A[i] -1] == A[i]: break
                    t = A[A[i] - 1] ; A[A[i] - 1] = A[i] ; A[i] = t
        for i, num in enumerate(A):
            if num != i + 1:
                return i + 1
        return length + 1
