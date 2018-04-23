class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False
        self.successors = {}

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        currentTrieNode = self.root
        for c in word:
            if c not in currentTrieNode.successors:
                currentTrieNode.successors[c] = TrieNode()
            currentTrieNode = currentTrieNode.successors.get(c)
        currentTrieNode.isEnd = True
    
    def searchHelper(self, word, currentTrieNode):
        if len(word) == 0:
            return currentTrieNode.isEnd
        for i, c in enumerate(word):
            if c != "." and c not in currentTrieNode.successors:
                return False
            if c == "." :
                result = None
                for successor in currentTrieNode.successors.values():
                    if self.searchHelper(word[i+1:], successor):
                        return True
                return False
            currentTrieNode = currentTrieNode.successors.get(c)
        return currentTrieNode.isEnd
            
    
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        currentTrieNode = self.root
        return self.searchHelper(word, currentTrieNode)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
