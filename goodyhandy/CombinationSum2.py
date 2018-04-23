class Solution(object):
    
    def dfs(self, candidates, currentSum, currentLst, target, solution, start):
        if currentSum >= target:
            if currentSum == target:
                solution.append(currentLst[:])
            return
        prev = None
        for i in xrange(start , len(candidates)):
            if candidates[i] != prev:
                currentLst.append(candidates[i])
                self.dfs(candidates, currentSum + candidates[i], currentLst, target, solution, i+1)
                currentLst.pop()
                prev = candidates[i]
        return 
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.positionMap = {}
        solution = []
        candidates.sort()
        self.dfs(candidates, 0, [], target, solution, 0 )
        return solution
