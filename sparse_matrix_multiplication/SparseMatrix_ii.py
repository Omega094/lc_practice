class Solution(object):
    def multiply_brute(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        rowNum = len(A); colNum = len(B[0])
        newMatrix = [[0 for i in xrange(colNum)] for j in xrange(rowNum)]
        iNum = len(A[0])
        print newMatrix
        for r in xrange(rowNum):
            for c in xrange(colNum):
                for i in xrange(iNum):
                    newMatrix[r][c] += A[r][i]*B[i][c]
        return newMatrix


#test
A = [[1,0,0],[-1,0,3]]
B = [[7,0,0], [0,0,0],[0,0,1]]
sol = Solution()
print sol.multiply_brute(A, B)
C = [[1,-5]]
D = [[12],[-1]]
print sol.multiply_brute(C,D)
