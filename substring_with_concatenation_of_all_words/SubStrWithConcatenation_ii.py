class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        numWords = len(words)
        wordLen = len(words[0])
        totalWordLen = numWords*wordLen
        result = []
        for i in xrange(0, len(s) - totalWordLen + 1):
            wordSet = set(words)
            for j in xrange(numWords):
                currentW = s[i+wordLen*j: i +wordLen*(j+1)]
                if currentW not in wordSet:
                    break
                wordSet.remove(currentW)
            if len(wordSet) == 0:
                result.append(i)
        return result

#test
sol = Solution()
print sol.findSubstring("barfoothefoobarman", ["foo", "bar"])
