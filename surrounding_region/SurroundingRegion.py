class Solution(object):
    
    def dfs(self,board, x, y):
        if x >= 0 and x < len(board[0]) and y >=0 and y <len(board):
            if board[y][x] == "O":
                board[y][x] = "E"
                self.dfs(board,x-1,y)
                self.dfs(board,x+1,y)
                self.dfs(board,x, y-1)
                self.dfs(board,x, y+1)
        return


    def bfs(self, board, x, y):
        queue = []
        queue.append((x, y))
        while queue:
            x, y = queue.pop(0)
            if x >= 0 and x < len(board[0]) and y >=0 and y <len(board):
                if board[y][x] == "O":
                    board[y][x] = "E"
                    queue.append((x-1,y))
                    queue.append((x+1,y))
                    queue.append((x, y-1))
                    queue.append((x, y+1))



    def solve(self, board, func):
        height = len(board)
        width = len(board[0])
        for i in xrange(height):
            func(board, 0, i)
            func(board, width-1, i)
        for j in xrange(width):
            func(board, j, 0)
            func(board, j, height-1)
        for x in xrange(width):
            for y in xrange(height):
                if board[y][x] == "O":
                    board[y][x] = "X"
                if board[y][x] == "E":
                    board[y][x] = "O"
        return
#test:
if __name__ == "__main__":
    board = [ [ 'X', 'X', 'X', 'X' ], [ 'X', 'O', 'O', 'X' ], [ 'X', 'X', 'O', 'X' ], [ 'X', 'O', 'X', 'X' ]]
    sol = Solution()
    sol.solve(board, sol.bfs)
    print board
    board = [ [ 'X', 'X', 'X', 'X' ], [ 'X', 'O', 'O', 'X' ], [ 'X', 'X', 'O', 'X' ], [ 'X', 'O', 'X', 'X' ]]
    sol.solve(board, sol.dfs)
    print board