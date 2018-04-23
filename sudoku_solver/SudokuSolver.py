class Solution(object):
    
    def getPositionsToFill(self, board):
        result = []
        for y in xrange(0, 9):
            for x in xrange(0, 9):
                if board[y][x] == '.':
                    result.append( (x, y))
        return result
    
    def isValid(self, board, x , y):
        temp = board[y][x]
        board[y][x] = "X"
        for i in range(9):
            if board[i][x] == temp:
                board[y][x] = temp
                return False
        for j in range(9):
            if board[y][j] == temp:
                board[y][x] = temp
                return False
        for i in range(3):
            for j in range(3):
                if board[(y//3)*3+i][(x//3)*3+j] == temp:
                    board[y][x] = temp
                    return False
        board[y][x] = temp
        return True

    def dfsSolverAndChecker(self,positions, board):
        for x, y in positions:
                if board[y][x] == '.':
                    for i in '123456789':
                        board[y][x] = i
                        if self.isValid(board, x, y) and self.dfsSolverAndChecker(positions, board):
                            return True
                        board[y][x] = '.'
                    return False
        return True


    def solveSudoku(self, board):
        positions = self.getPositionsToFill(board)
        self.dfsSolverAndChecker(positions, board)
