class Solution(object):
    def DFS(self, target, k ,currentSum, currentNum, currentList,solution):
        if len(currentList) > k: return 
        if len(currentList)==k :
            if currentSum == target:
                solution.append(currentList)
            return 
        for i in range(currentNum+1, 10):
            self.DFS(target, k,currentSum+i, i, currentList + [i], solution) 





    def combinationSum3(self, k, n):
        solution = []
        self.DFS(n, k, 0, 0, [], solution )
        return solution


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.combinationSum3(3, 9)
