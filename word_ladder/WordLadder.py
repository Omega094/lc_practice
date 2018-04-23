class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList = set(wordList)
        visited = set([beginWord])
        queue = [beginWord]
        distance = 1
        while queue:
            for _ in xrange(len(queue)):
                currentNode = queue.pop(0)
                for c in "abcdefghijklmnopqrstuvwxyz":
                    for i in xrange(0, len(currentNode)):
                        nextWord = currentNode[:i]+c+currentNode[i+1:]
                        if nextWord in wordList and nextWord not in visited:
                            if nextWord == endWord: return distance + 1
                            visited.add(nextWord)
                            queue.append(nextWord)
            distance += 1
        return 0
                            
