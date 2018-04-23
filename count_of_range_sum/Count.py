class tree(object):
    def __init__(self, size):
        self.tree = [0]*(size+1)
        self.treeSize = len(self.tree)
    
    def update(self,index):
        while index < self.treeSize:
            self.tree[index] += 1
            index += (index & -index)
        return
    
    def query(self, index):
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= (index & -index)
        return s
        
        
        
        
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums: return 0

        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        for i in xrange(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        sortedNum = [upper, lower-1]
        for num in prefix:
            sortedNum += [num, num+lower-1, num+upper]
        sortedNum.sort()
        numToIndex = {num : i for i, num in enumerate(sortedNum, 1) }
        bit = tree(len(sortedNum))
        count = 0
        currentSum = prefix[-1]
        for j in xrange(len(prefix) -1 , - 1, -1):
            bit.update(numToIndex[currentSum])
            currentSum -= nums[j]
            count += bit.query(numToIndex[currentSum+upper]) - bit.query(numToIndex[currentSum+lower-1])
        return count

