#Fast version of building a trie.

class Trie(object):

    def __init__(self):
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        currentTrieNode = self.root
        for c in word:
            if c not in currentTrieNode:
                currentTrieNode[c] = {}
            currentTrieNode = currentTrieNode.get(c)
        #if a node has the key "#" that means it is an endpoint. 
        #Note: We are assumming that word does not contain "#"
        currentTrieNode["#"] = {}
        
    def traverse(self, result, currentWord, currentNode):
        if "#" in currentNode:
            result.append(currentWord)
        for c in currentNode.keys():
            if c == "#": continue
            self.traverse(result, currentWord + c, currentNode[c])
        return 

    def typeAhead(self, head):
        currentTrieNode = self.root
        if not self.startsWith(head):
            return None
        for c in head:
            currentTrieNode = currentTrieNode[c]
        result = []
        for c in currentTrieNode.keys():
            if c == "#": continue
            self.traverse(result, head+c, currentTrieNode[c])
        return result 

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currentTrieNode = self.root
        for c in word:
            if c not in currentTrieNode:
                return False
            currentTrieNode = currentTrieNode.get(c)
        return currentTrieNode.has_key("#")

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currentTrieNode = self.root
        for c in prefix:
            if c not in currentTrieNode:
                return False
            currentTrieNode = currentTrieNode.get(c)
        return True
        
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
trie = Trie()
trie.insert("ABCD")
trie.insert("ABCDE")
print trie.search("ABCDEFG")
print trie.search("ABCD")
print trie.search("DEFG")
print trie.root
print trie.typeAhead("ABC")
