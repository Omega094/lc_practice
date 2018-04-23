class Solution(object):
    def subsetHelper(self, currentLst, remainLst, k,solution):
        if len(currentLst) == k:
            solution.append(currentLst)
            return 
        for i in xrange(0, len(remainLst)):
            self.subsetHelper(currentLst + [remainLst[i]], remainLst[i+1:], k , solution)
        return 
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = [[]]
        k = len(nums)
        for i in xrange(1,k + 1):
            self.subsetHelper([], nums, i, solution)
        return solution 
        
        
