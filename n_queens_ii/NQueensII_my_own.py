class Solution(object):
    def solveNQueensHelper(self, n, colLst):
        if len(colLst) == n:
            self.solution += 1
            return
        currentRow = len(colLst)
        for i in xrange(0, n):
            if i not in colLst :
                attack = False
                for j in xrange(0, len(colLst)):
                    if currentRow - j == abs(i - colLst[j]):
                        attack = True
                if not attack:
                    self.solveNQueensHelper(n, colLst + [i])
        return


    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.solution = 0
        self.solveNQueensHelper(n , [])
        return self.solution
 
        
