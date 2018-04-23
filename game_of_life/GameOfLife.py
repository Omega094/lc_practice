class Solution(object):
 
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #This is a nice way to get neighbours
        dx = (1,1,1,0,0,-1,-1,-1)
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for x in xrange(0, len(board[0])):
            for y in xrange(0, len(board)):
                #For each cell, check neighbours
                livesAround = 0
                for i in range(0, 8):
                    nx, ny = x + dx[i], y + dy[i]
                    livesAround += self.getCellNextstatus(nx, ny, board)
                if livesAround == 3 or board[y][x] + livesAround == 3:
                    board[y][x] |= 2
        #Now we update the board by shifting each val on bit right.
        for x in xrange(0, len(board[0])):
            for y in xrange(0, len(board)):
                board[y][x] >>= 1

    def getCellNextstatus(self, x, y, board):
        if x < 0 or y < 0 or y >= len(board) or x >= len(board[0]):
            return 0
        return board[y][x] & 1

