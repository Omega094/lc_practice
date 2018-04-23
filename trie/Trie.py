class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False
        self.successors = {}
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        currentTrieNode = self.root
        for c in word:
            if c not in currentTrieNode.successors:
                currentTrieNode.successors[c] = TrieNode()
            currentTrieNode = currentTrieNode.successors.get(c)
        currentTrieNode.isEnd = True
        
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currentTrieNode = self.root
        for c in word:
            if c not in currentTrieNode.successors:
                return False
            currentTrieNode = currentTrieNode.successors.get(c)
        return currentTrieNode.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currentTrieNode = self.root
        for c in prefix:
            if c not in currentTrieNode.successors:
                return False
            currentTrieNode = currentTrieNode.successors.get(c)
        return True
        
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
