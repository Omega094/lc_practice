class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        #build a graph with successor and predecessor
        from collections import defaultdict
        successor = defaultdict(set)
        predecessor = defaultdict(set)
        pairs = zip(words, words[1:])
        for pair in pairs:
            for a, b in zip(*pair):
                if a != b:
                    successor[a].add(b)
                    predecessor[b].add(a)
                    #if current digit not equal, no need to 
                    #compare the rest.
                    break
        allChar = set(''.join(words))
        #If the char have predecessor, 
        #then it cannot be the char to start with. 
        #Actually we can pop a set....no need to convert to list.
        startChars = list(allChar - set(predecessor))
        result = ""
        while startChars:
            c = startChars.pop(0)
            result += c
            for child in successor[c]:
                predecessor[child].remove(c)
                if not predecessor[child]:
                    startChars.append(child)
        return result if set(result) == allChar else ""
        

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.alienOrder(["wrt","wrf","er","ett","rftt"])
