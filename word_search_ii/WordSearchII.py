class Solution(object):

    def __init__(self):
        self.solutionList = []

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        #The tricky part here is that the list of words can be huge. 
        #So it would be better to use a trie to save it. 
        self.solutionList = []
        trie = {}
        for word in words:
            currentTrieNode = trie 
            for c in word:
                if c not in currentTrieNode:
                    currentTrieNode[c] = {}
                currentTrieNode = currentTrieNode[c]
            currentTrieNode["#"] = {}
        print trie
        currentTrieNode = trie
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                    if board[i][j] in currentTrieNode:
                        self.searchHelper(board, j, i, board[i][j],currentTrieNode[board[i][j]])
        return list(set(self.solutionList ))

    def searchHelper(self, board, currentX, currentY ,currentWord, currentTrieNode):
        if currentY >= len(board) or currentY < 0 or currentX >= len(board[0]) or currentX < 0:
                return
        if currentTrieNode.has_key("#"):
            self.solutionList.append(currentWord)
        temp = board[currentY][currentX] 
        board[currentY][currentX] = None
        if currentX-1 >=0 :
            if board[currentY][currentX-1] and board[currentY][currentX-1] in currentTrieNode:
                currentChar = board[currentY][currentX-1]  
                self.searchHelper(board, currentX-1, currentY, currentWord + currentChar, currentTrieNode[currentChar]) 
        if currentX+1 < len(board[0]):
            if board[currentY][currentX+1] and board[currentY][currentX+1] in currentTrieNode:
                currentChar = board[currentY][currentX+1]  
                self.searchHelper(board, currentX+1, currentY, currentWord + currentChar, currentTrieNode[currentChar]) 
        if currentY-1 >=0 :
            if board[currentY-1][currentX] and board[currentY-1][currentX] in currentTrieNode:
                currentChar = board[currentY-1][currentX]  
                self.searchHelper(board, currentX, currentY-1, currentWord + currentChar, currentTrieNode[currentChar]) 
        if currentY+1 < len(board):
            if board[currentY+1][currentX] and board[currentY+1][currentX] in currentTrieNode:
                currentChar = board[currentY+1][currentX]  
                self.searchHelper(board, currentX, currentY+1, currentWord + currentChar, currentTrieNode[currentChar]) 
        board[currentY][currentX] = temp
        return 


#test
if __name__ == "__main__":
    words = ["oath","pea","eat","rain"]
    board =[['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
    sol = Solution()
    print sol.findWords(board, words)



