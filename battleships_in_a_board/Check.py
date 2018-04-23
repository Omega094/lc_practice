class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0 
        for y in xrange(len(board)):
            for x in xrange(len(board[0])):
                if board[y][x] == "X":
                    if (x >=1 and board[y][x-1] == "X") or (y >= 1 and board[y-1][x] == "X"): continue
                    count += 1
        return count
                
