# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    
    def depthSumInverseHelper(self, currentList, currentLevel, levelDict):
        currentSum = 0
        nestedSum = []
        for nested in currentList:
            if not nested.isInteger():
                self.depthSumInverseHelper(nested.getList(), currentLevel+1, levelDict)
            else:
                currentSum += nested.getInteger()
        if self.setted < currentLevel:
            self.setted = currentLevel
        levelDict[currentLevel] = levelDict.get(currentLevel,0) + currentSum
        
    
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.setted = 0
        levelDict = dict()
        self.depthSumInverseHelper(nestedList, 1,levelDict)
        result = 0
        for level, val in levelDict.iteritems():
            result += val*(self.setted - level+1)
        return result

