#Step 1 sort
#Step 2: call recursive dfs
#iterate each value in list.

class Solution(object):
    
    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in Solution.ret:
            return Solution.ret.append(valuelist)
        #Avoids duplicate 
        for i in range(start, length):
            if target < candidates[i]:
                return
            #Can start from the same position. but not 0
            #If each number can only be used once , change the i to i +1 
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])
        
    def combinationSum(self, candidates, target):
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret


#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.combinationSum([2,3,6,7], 7)

