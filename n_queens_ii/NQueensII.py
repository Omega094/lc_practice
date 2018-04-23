class Solution(object):


    #helper function that
    #1 checks if the current board is valid.
    #2 appends a new row
    #3 append solution to solution list if the solution is valid.

    def nQueensHelper(self, boardSize,  occupyList):
        if len(occupyList) == boardSize:
            self.solutionSize += 1
            return
        currentLineNum = len(occupyList)
        for i in range (0, boardSize):
            valid = True
            for j in range(0, len(occupyList)):
                if i in  occupyList : valid = False; break
                if abs(currentLineNum - j) == abs(i - occupyList[j]):
                    valid = False; break
            if valid:
                newList = occupyList[:]+[i]
                self.nQueensHelper(boardSize, newList)

    def totalNQueens(self, n):
        self.solutionSize = 0
        occupyList = []
        self.nQueensHelper(n , occupyList)
        return self.solutionSize 


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.totalNQueens(4)

