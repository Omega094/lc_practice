class Solution(object):

    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in Solution.ret:
            return Solution.ret.append(valuelist)
        #Avoids duplicate
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i+1, valuelist + [candidates[i]])

    def combinationSum(self, candidates, target):
        candidates.sort()
        print candidates
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret


#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.combinationSum([10,1,2,7,6,1,5], 8)

