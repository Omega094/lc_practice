class Solution(object):
    def fingSubstring(self, s, words):
        result = []
        from collections import Counter
        singleWordLen = len(words[0])
        totalWordLen = len(words)*singleWordLen
        for i in xrange(singleWordLen):
            wordCounter = Counter(words)
            backPtr = i
            for j in xrange(i, len(s), singleWordLen):
                currentWord = s[j:j + singleWordLen]
                wordCounter[currentWord] -= 1
                while wordCounter[currentWord] < 0:
                    wordCounter[s[backPtr: backPtr + singleWordLen]] += 1
                    backPtr += singleWordLen
                if j - backPtr + singleWordLen == totalWordLen:
                    result.append(backPtr)
        return result 

#test
sol = Solution()
print sol.fingSubstring("barfoothefoobarman", ["foo", "bar"])


