class Solution(object):
    
    def groupAnagrams(self, strs):
        from collections import defaultdict
        wordDict = defaultdict(list)
        #remove duplicates first
        for word in strs:
            key = "".join(sorted([c for c in word]))
            wordDict[key].append(word)
            wordDict[key].sort()
        return wordDict.values()

#test
if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print sol.groupAnagrams(words)


