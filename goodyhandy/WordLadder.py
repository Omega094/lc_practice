class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        from collections import deque
        queue = deque([beginWord])
        distance = 1
        visited = set([beginWord])
        while queue: 
            #length = len(queue)
            for _ in xrange(len(queue)):
                current = queue.popleft()
                #if current == endWord: return distance
                for j in xrange(len(current)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nextWord = current[:j] + c + current[j+1:]
                        if nextWord == endWord: return distance + 1
                        if nextWord in wordList and nextWord not in visited:
                            queue.append(nextWord)
                            visited.add(nextWord)
            distance += 1
        return 0
sol = Solution()
print sol.ladderLength("hit", "cog", set(["hot","dot","dog","lot","log"]))
