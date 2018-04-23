class Solution(object):

    def findSubstring(self, S, L):
        singleWordLength = len(L[0])
        solution = []
        numWords = len(L)
        for i in range (0, len(S) - singleWordLength*numWords + 1):
            wordSet = set(L)
            wordChunk = S[i : i + singleWordLength*numWords]
            for j in range(0, len(wordChunk) ,singleWordLength):
                currentWord = wordChunk[j: j + singleWordLength]
                if currentWord in wordSet:
                    wordSet.remove(currentWord)
                else:
                    break
            if len(wordSet) == 0:
                solution.append(i)
        return solution
    
    #Sliding window solution. 
    #Same idea as sliding window !!!
    #The back of window is "start" variable. 
    #The complexity is O(k*n)
    def findSubstring_efficient(self, S, L):
        import collections
        import copy
        singleWordLength = len(L[0])
        numWords = len(L)
        totalWordlen = singleWordLength*numWords
        solution = []
        #Counter is a good thing !
        wordCounter = collections.Counter(L)
        #start of word can only be in position of 0 to single wordlength.
        for i in range (0, singleWordLength):
            tempDict = copy.deepcopy(wordCounter)
            start = i
            for j in range (i, len(S) - singleWordLength + 1, singleWordLength):
                currentWord = S[j:j+singleWordLength]
                tempDict[currentWord] = tempDict.get(currentWord, 0) - 1
                #Renew the window once the current window cannot become valid.
                while tempDict[currentWord] < 0:
                    tempDict[S[start: start + singleWordLength]] += 1
                    start += singleWordLength
                #Check the result
                if (j - start + singleWordLength) == totalWordlen:
                    solution.append(start)
        return solution
    


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.findSubstring("barfoothefoobarman", ["foo", "bar"])
    print sol.findSubstring_efficient("barfoothefoobarman", ["foo", "bar"])
