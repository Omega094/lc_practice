class Solution(object):
    def gameOfLife(self, board):
        dx = (1,1,1,0,0,-1,-1,-1)
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for y in xrange(0, len(board)):
            for x in xrange(0, len(board[0])):
                livesAround = 0
                for i in xrange(8):
                    nx , ny = x + dx[i], y + dy[i]
                    livesAround += self.check(nx, ny, board)
                if livesAround ==3 or livesAround + board[y][x] == 3:
                    board[y][x] |= 2
        for y in xrange(0, len(board)):
            for x in xrange(0, len(board[0])):
                board[y][x] >>= 1
        return 

    def check(self,x,y,board):
        if x<0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return 0
        return board[y][x] & 1
