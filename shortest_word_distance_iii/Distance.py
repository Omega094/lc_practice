class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1Index = None
        word2Index = None
        minDistance = float('inf')
        for i, word in enumerate(words):
            if word == word1:
                temp = word1Index
                word1Index = i
                #print word1Index
                if word2Index != None:
                    minDistance =min(minDistance, word1Index - word2Index)
                if temp != None and word1 == word2:
                    minDistance =min(minDistance, word1Index - temp)
            elif word == word2 :
                word2Index = i
                #print word2Index
                if word1Index != None:
                    minDistance = min(minDistance, word2Index - word1Index)
        return minDistance
