class Solution(object):
    
    def solveNQueensHelper(self, n, currentBoard, colLst, solution):
        if len(currentBoard) == n:
            solution.append(currentBoard)
            return
        currentRow = len(currentBoard)
        for i in xrange(0, n):
            if i not in colLst :
                attack = False
                for j in xrange(0, len(colLst)):
                    if currentRow - j == abs(i - colLst[j]):
                        attack = True
                if not attack:
                    self.solveNQueensHelper(n, currentBoard + ["."*(i)+"Q"+"."*(n-i-1)], colLst + [i], solution)
        return 


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solution = []
        self.solveNQueensHelper(n , [], [], solution)
        return solution
#test
sol = Solution()
print sol.solveNQueens(4)
        
