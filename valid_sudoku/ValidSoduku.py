class Solution(object):

    def isValidSudoku(self, board):
        mem_row = [{}for i in range(0, 9)]
        mem_col = [{}for j in range(0, 9)]
        mem_square = [[{},{},{}]for k in range(0,3)]
        #dosen't matter what you put into the dictionary
        for i in range (0, 9):
            for j in range (0, 9):
                char = board[i][j] 
                if char in mem_row[i] or char in mem_col[j] or char in mem_square[i//3][j//3]: return False
                if char != '.': 
                    mem_row[i][char] = (i,j)
                    mem_col[j][char] = (i,j)
                    mem_square[i//3][j//3][char] = (i,j)
        return True


#test
if __name__ == "__main__":
    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    sol = Solution()
    print sol.isValidSudoku(board)
    
