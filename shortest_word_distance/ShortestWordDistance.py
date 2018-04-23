class Solution(object):
    def shortestDistance(self, words, word1, word2):
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
                word1Index = i
                #print word1Index
                if word2Index != None:
                    minDistance =min(minDistance, word1Index - word2Index)
            elif word == word2:
                word2Index = i
                #print word2Index
                if word1Index != None:
                    minDistance = min(minDistance, word2Index - word1Index)
        return minDistance

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"makes", "coding")
