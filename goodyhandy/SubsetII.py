class Solution(object):
    def subsetHelper(self, currentLst, remainLst, k,solution):
        if len(currentLst) == k:
            solution.append(currentLst)
            return 
        prev = None
        for i in xrange(0, len(remainLst)):
            if remainLst[i] == prev: continue
            prev = remainLst[i]
            self.subsetHelper(currentLst + [remainLst[i]], remainLst[i+1:], k , solution)
        return 
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        solution = [[]]
        k = len(nums)
        for i in xrange(1,k + 1):
            self.subsetHelper([], nums, i, solution)
        return solution 
        
        
