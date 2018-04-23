class Solution(object):
        
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = float(sum(nums))/2
        if target > int(target):
            return False
        target = int(target)
        table = [False]*(target+1)
        table[0] = True
        for n in nums:
            for i in xrange(target, -1, -1):
                if table[target] : return True
                if i-n >=0 and not table[i]  and table[i - n]  :
                    table[i] = True
        return table[-1] 
        
        
        
