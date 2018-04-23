class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        rowNum = len(A); colNum = len(B[0])
        newMatrix = [[0 for i in xrange(colNum)] for j in xrange(rowNum)]
        iNum = len(A[0])
        ASparseTable = set([i for i in xrange(rowNum) if not any(A[i]) ])
        BSparseTable = set([j for j in xrange(colNum) if not any ( [B[k][j] for k in xrange(len(B))])])
        for r in xrange(rowNum):
            for c in xrange(colNum):
                if r in ASparseTable or c in BSparseTable:
                    newMatrix[r][c] = 0
                    continue 
                for i in xrange(iNum):
                    newMatrix[r][c] += A[r][i]*B[i][c]
        return newMatrix
