class Solution(object):
    def exist(self, board, word):
        if len(word) > len(board)*len(board[0]): return False
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                    if self.searchHelper(board, j, i, word):
                        return True
        return False

    def searchHelper(self, board, currentX, currentY ,word):
        if len(word) == 0: return True
        if currentY >= len(board) or currentY < 0 or currentX >= len(board[0]) or currentX < 0:
                return False
        if not board[currentY][currentX] or board[currentY][currentX] != word[0]: return False
        temp = board[currentY][currentX]
        """
        We don't want to allocate extra board to increase time/space cost. 
        """
        board[currentY][currentX] = None
        valid = False
        valid= self.searchHelper(board, currentX -1 , currentY, word[1:]) or \
               self.searchHelper(board, currentX +1 , currentY, word[1:]) or \
               self.searchHelper(board, currentX , currentY-1, word[1:]) or \
               self.searchHelper(board, currentX , currentY+1, word[1:])
        '''Restore the board'''
        board[currentY][currentX] = temp
        return valid
        

#test:
if __name__ == "__main__":
    board = [ ['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = "ABCCED"
    sol = Solution()
    print sol.exist(board, word)
    print sol.exist(board, "SEE")
    print sol.exist(board, "ABCB")
    import profile
    profile.run('sol.exist(board, "ABCB")')
