class Solution(object):
    
    
    def dfs(self, currentLst, currentResult, target):
        if currentResult == target: return True
        if currentResult > target: return False
        for i in xrange(0, len(currentLst)):
            if self.dfs(currentLst[:i]+currentLst[i+1:], currentResult + currentLst[i], target):
                return True
        return False
        
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = float(sum(nums))/2
        if target > int(target):
            return False
        return self.dfs(nums, 0, target)
        
        
        
