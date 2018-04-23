class Solution(object):

    def check(self, s, wordDict):
        lst = [False for i in range(len(s) + 1)]
        lst[0] = True
        for i in range(1, len(s) +1):
            for j in range(0, i):
                if lst[j] == True and s[j:i] in wordDict:
                    lst[i] = True
        return lst[len(s)] == True
    
    def dfs(self, s, wordDict, currentWord, solutionList):
        if self.check(s, wordDict):
            if s == "":
                solutionList.append(currentWord[1:])
                return
            for i in range(1, len(s)+1):
                print s[:i]
                if s[:i] in wordDict:
                    self.dfs(s[i:],wordDict, currentWord+" "+s[:i],solutionList)
            return

    def wordBreak(self, s, wordDict):
        solutionList = []
        self.dfs(s, wordDict, "", solutionList)
        return solutionList

#test:
if __name__ == "__main__":
    sol = Solution()
    s = "catsanddog"
    wordDict = set(["cat", "cats", "and", "sand", "dog"])
    print sol.wordBreak(s, wordDict)
