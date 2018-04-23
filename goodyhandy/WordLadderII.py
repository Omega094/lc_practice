class Solution(object):
    def findLadders(self, start, end, wordlist):
        wordlist.add(start)
        wordlist.add(end)
        result = []
        from collections import defaultdict
        trace = defaultdict(list)
        visited = set()
        found = False; queue = set([start])
        while queue and not found:
            #currentWord = queue.pop(0)
            #Has to be level by level, 
            #Otherwise it will not return complete result 
            nextQueue = set()
            for currentWord in queue:
                visited.add(currentWord)
            for currentWord in queue:
                for i in xrange(len(currentWord)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = currentWord[:i] + c + currentWord[i+1:]
                        if newWord in wordlist and newWord not in visited:
                            nextQueue.add(newWord)
                            trace[newWord].append(currentWord)
                            if newWord == end:
                                found = True
            queue = nextQueue
        if found:
            self.backtrack(result,   trace, [], end)
        return result

    def backtrack(self, result, trace, path, word):
        if len(trace[word]) == 0:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)

#test
sol = Solution()
print sol.findLadders("hit", "cog", set(["hot","dot","dog","lot","log"]))
