class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wordToIndex = {w: i for i, w in enumerate(words)}
        result = []
        for i , w in enumerate(words):
            for j in xrange(0, len(w)+1):
                left = w[:j]
                right = w[j:]
                if left == left[::-1]:
                    if wordToIndex.has_key(right[::-1]) and wordToIndex[right[::-1]] != i :
                        result.append((wordToIndex[right[::-1]], i))
                if right == right[::-1]:
                    if wordToIndex.has_key(left[::-1]) and wordToIndex[left[::-1]] != i:
                        result.append((i,wordToIndex[left[::-1]]))
        return list(set(result))

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.palindromePairs(["bat", "tab", "cat"])
