class Solution(object):
    
    
    def searchHelper(self, board, x, y, i):
        if board[y][x] == self.target[i] and i == len(self.target) - 1 :
            return True
        if board[y][x] != self.target[i] : return False
        self.visited.add((x, y))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nextX, nextY = x + dx, y + dy
            if nextX >= 0 and nextX < self.width and nextY >= 0 and nextY < self.height and (nextX, nextY) not in self.visited:
                if self.searchHelper(board, nextX, nextY, i + 1): return True
        self.visited.remove((x, y))
        return False
    
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0: return True
        self.target = word
        self.width = len(board[0])
        self.height = len(board)
        for y in xrange(self.height):
            for x in xrange(self.width):
                self.visited = set()
                if self.searchHelper(board, x, y, 0): return True
        return False
