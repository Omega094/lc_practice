class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        wordList = set(wordList)
        visited = set([beginWord])
        queue = set([beginWord])
        from collections import defaultdict
        graph = defaultdict(set)
        found = False
        while queue and not found:
            nextQueue = set()
            for c in queue:
                visited.add(c)
            for currentNode in queue:
                for c in "abcdefghijklmnopqrstuvwxyz":
                    for i in xrange(0, len(currentNode)):
                        nextWord = currentNode[:i]+c+currentNode[i+1:]
                        if nextWord in wordList and nextWord not in visited:
                            if nextWord == endWord: found = True
                            graph[nextWord].add(currentNode)
                            nextQueue.add(nextWord)
            queue = nextQueue
            
        def backTrack(ew, g, path, sol):
            if len(g[ew]) == 0: 
                sol.append(path); return
            for w in graph[ew]:
                backTrack(w, g, [w]+path, sol)
        
        solution = []
        if found:
            backTrack(endWord, graph, [endWord], solution)
        return solution        
