class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict
        successor = defaultdict(set)
        predecessor = defaultdict(set)
        pairs = [(words[i], words[i+1]) for i in xrange(len(words) - 1)]
        for a, b in pairs:
            for i in xrange(min(len(a), len(b))):
                if a[i] != b[i]:
                    successor[a[i]].add(b[i])
                    predecessor[b[i]].add(a[i])
                    break
        #Now we start the topology sort.
 
        result = []
        total = set()
        for word in words:
            for c in word:
                total.add(c)
        queue = [ c for c in total if len(predecessor[c]) == 0]
 
        #result += queue
        while queue:
            c = queue.pop(0)
            result.append(c)
            for child in successor[c]:
                #print predecessor[child]
                predecessor[child].remove(c)
                if len(predecessor[child]) == 0:
                    queue.append(child)
        return "".join(result) if len(result) == len(total) else ""
#test
sol = Solution()
print sol.alienOrder(["wrt","wrf","er","ett","rftt"])
