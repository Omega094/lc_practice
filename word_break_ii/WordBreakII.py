class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    
    def check(self, s, dict):
        list = [False for i in range (len(s)+ 1)]
        list[0] = True
        for i in range (1, len(s)+1):
            for j in range (0, i):
                if list[j]== True and s[j:i] in dict:
                    list[i]= True
        return list[len(s)] == True

    def dfs(self, s, dict, solutionList):
        if self.check(s, dict):
            if len(s) == 0:
                self.solution.append(solutionList[1:])
            for i in range (1, len(s)+1):
                if s[:i] in dict:
                    self.dfs(s[i:],dict, solutionList +' '+ s[:i])

    def wordBreak(self, s, dict):
        self.solution = []
        self.dfs(s, dict, '')
        return self.solution

#test
if __name__ == "__main__":
    sol = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print sol.wordBreak(s, wordDict)
