class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict
        degree = defaultdict(int)
        currentToNext = defaultdict(set)
        pairs = set()
        cSet = set()
        for w in words:
            for c in w:
                cSet.add(c)
        for i in xrange(0, len(words)-1):
            pairs.add((words[i], words[i+1]))
        for a, b in pairs:
            for i in xrange(0, min(len(a), len(b))):
                if a[i] != b[i] and b[i] not in currentToNext[a[i]] : 
                    currentToNext[a[i]].add(b[i])
                    degree[b[i]] += 1
                    break
        queue = [a for a in cSet if a not in degree]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current)
            for child in currentToNext[current]:
                degree[child] -= 1
                if degree[child] == 0:
                    queue.append(child)
        return "".join(result) if len(result) == len(cSet) else ""
        
        
                
