#Time has to be constant. 
#Time O(1)
#Space O(n) 
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        #we don't care about the board state, only care about the result
        self.size = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagnal = 0
        self.antidiagnal = 0

    def move(self, row, col, player):
        #This is the most important part. 
        #To use a delta. 
        delta = 1 if player == 1 else -1
        self.rows[row] += delta
        self.cols[col] += delta
        if (row == col): self.diagnal += delta
        if (col == (self.size - row - 1)): self.antidiagnal += delta
        if (abs(self.rows[row]) == self.size or abs(self.cols[col]) == self.size or abs(self.diagnal) == self.size or abs(self.antidiagnal) == self.size): return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
