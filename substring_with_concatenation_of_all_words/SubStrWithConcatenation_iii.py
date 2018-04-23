class Solution(object):
    def findSubstring(self, S, L):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        import collections
        import copy
        singleWordLength = len(L[0])
        numWords = len(L)
        totalWordlen = singleWordLength*numWords
        solution = []
        #Counter is a good thing !
        wordCounter = collections.Counter(L)
        #start of word can only be in position of 0 to single wordlength.
        for i in range(0, singleWordLength):
            tempDict = copy.deepcopy(wordCounter)
            backPtr = i
            for j in range(i, len(S) - singleWordLength + 1, singleWordLength):
                currentW = S[j:j+singleWordLength]
                tempDict[currentW]  = tempDict[currentW] - 1
                while tempDict[currentW] < 0:
                    tempDict[S[backPtr: backPtr + singleWordLength]] += 1
                    backPtr += singleWordLength
                if (j - backPtr + singleWordLength) == totalWordlen:
                    solution.append(backPtr)
        return solution
