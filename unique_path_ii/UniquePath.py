class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        board = []
        for i in range (0,m):
            board.append([0 for j in range (0,n)])
        board[0][0] = 1
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1  : return 0
        for rowNum in range (0, m):
            for colNum in range (0, n):
                if rowNum != 0 and colNum != 0:
                    if obstacleGrid[rowNum-1][colNum] == 0 and obstacleGrid[rowNum][colNum-1]==0:
                        board[rowNum][colNum] += board[rowNum][colNum-1] + board[rowNum -1][colNum]
                    elif obstacleGrid[rowNum-1][colNum] == 0 and obstacleGrid[rowNum][colNum-1]==1:
                         board[rowNum][colNum] = board[rowNum-1][colNum]
                    elif obstacleGrid[rowNum-1][colNum] == 1 and obstacleGrid[rowNum][colNum-1]==0:
                         board[rowNum][colNum] = board[rowNum][colNum - 1]
                elif rowNum!=0 and colNum == 0:
                    if obstacleGrid[rowNum-1][colNum] == 0:
                        board[rowNum][colNum] = board[rowNum-1][colNum]
                elif rowNum ==0 and colNum !=0:
                    if obstacleGrid[rowNum][colNum - 1] == 0:
                        board[rowNum][colNum] = board[rowNum][colNum -1]
        return board[m-1][n-1]



#test:
if __name__ == "__main__":
    board = [[0,0,0],[0,1,0],[0,0,0]]
    sol = Solution()
    print sol.uniquePathsWithObstacles(board)

