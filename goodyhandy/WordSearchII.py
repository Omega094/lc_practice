class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        #Quickly build the prefix tree
        if not board or not words: return []
        self.trie = {}
        for word in words:
            currentNode = self.trie
            for c in word:
                if c not in currentNode:
                    currentNode[c] = {}
                currentNode = currentNode[c]
            currentNode['#'] = {}
        self.width, self.height, self.solution = len(board[0]), len(board), []
        for y in xrange(self.height):
            for x in xrange(self.width):
                self.visited = set()
                if board[y][x] in self.trie:
                    self.searchHelper(board, self.trie[board[y][x]], x, y, board[y][x])
        return list(set(self.solution))
    
    def searchHelper(self, board, curNode, x, y, currentWord):
        if curNode.has_key('#'):
            self.solution.append(currentWord)
        self.visited.add((x, y))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            nextX, nextY = x + dx, y + dy
 
            if nextX >= 0 and nextY >= 0 and nextX < self.width and nextY < self.height and curNode.has_key(board[nextY][nextX]) and (nextX, nextY) not in self.visited :
                self.searchHelper(board, curNode[board[nextY][nextX]], nextX, nextY, currentWord + board[nextY][nextX])
        self.visited.remove((x, y))
        return 
