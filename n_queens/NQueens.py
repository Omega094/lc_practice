class Solution(object):
    
    #helper function that
    #1 checks if the current board is valid. 
    #2 appends a new row 
    #3 append solution to solution list if the solution is valid. 

    def nQueensHelper(self, boardSize, currentBoard, solutionList, occupyList):
        if len(currentBoard) == boardSize:
            solutionList.append(currentBoard)
            return
        currentLineNum = len(currentBoard)
        for i in range (0, boardSize):
            valid = True
            for j in range(0, len(occupyList)):
                if i in  occupyList : valid = False; break
                if abs(currentLineNum - j) == abs(i - occupyList[j]): 
                    valid = False; break 
            if valid:
                currentLine = i*'.'+'Q'+(boardSize-i-1)*'.'
                newBoard = currentBoard[:] + [currentLine]
                newList = occupyList[:]+[i]
                self.nQueensHelper(boardSize, newBoard, solutionList, newList)

    def solveNQueens(self, n):
        currentBoard = []
        solutionList = []
        occupyList = []
        self.nQueensHelper(n, currentBoard, solutionList, occupyList)
        return solutionList

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.solveNQueens(4)

