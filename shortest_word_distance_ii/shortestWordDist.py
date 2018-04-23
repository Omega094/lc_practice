class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        from collections import defaultdict
        self.positionDict = defaultdict(list)
        for i, word in enumerate(words):
            if word in self.positionDict:
                self.positionDict[word].append(i)
            else:
                self.positionDict[word] = [i]
        return 
    
    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 =[ (index, word1) for index in self.positionDict[word1]]
        l2 = [ (index, word2) for index in self.positionDict[word2]]
        #merge two sorted array
        result = []
        while l1 and l2:
            if l1[0][0] < l2[0][0]:
                result.append(l1.pop(0))
            else:
                result.append(l2.pop(0))
        if l2:
            l1 = l2
        result = result + l1
        print result
        dict = {}
        front = 0
        back = 0
        minDist = float('inf')
        while front < len(result):
            dict[result[front][1]] = result[front][0]
            if len(dict) < 2:
                front += 1
                continue
            print dict
            minDist =min(minDist, abs(dict[word1] - dict[word2]))
            while len(dict)==2:
                if result[back][0] in dict.values():
                    if result[back][0] == dict[word1]:
                        del dict[word1]
                    else:
                        del dict[word2]
                back += 1
            front += 1
            print dict, "After maintain"
        return minDist 
        
    #think about the while loop, 
    #Two pointer chasing each other
    def shortest_clean(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        aIdx = self.positionDict[word1]
        bIdx = self.positionDict[word2]
        i = j = 0
        minDist = float('inf')
        while i < len(aIdx) and j < len(bIdx):
            minDist = min(minDist, abs(aIdx[i] - bIdx[j]))
            if aIdx[i] < bIdx[j]:
                i += 1
            else:
                j += 1
        return minDist 

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")


if __name__ == "__main__":
    wd = WordDistance(["the","quick","brown","fox","quick"])
    print wd.shortest("quick","fox")
    print wd.shortest_clean("quick","fox")



