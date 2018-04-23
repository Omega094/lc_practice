class Solution(object):
    
    def search(self, lst,k, currentSum, target, solution):
        if len(lst) == k:
            if currentSum == target:
                solution.append(lst)
            return
        for i in xrange(lst[-1]+1, 10):
            self.search(lst+[i], k, currentSum+i, target, solution)
        return 
    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        target = n
        solution = []
        if k > n: return []
        for i in xrange(1, 10):
            self.search([i], k, i, target, solution)
        return solution
