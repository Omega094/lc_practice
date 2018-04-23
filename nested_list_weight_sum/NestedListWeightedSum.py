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
    
    def depthSumHelper(self, nestedList, level):
        for nestedInteger in nestedList:
            if nestedInteger.isInteger():
                self.sum += level*nestedInteger.getInteger()
            else:
                self.depthSumHelper(nestedInteger.getList(), level + 1)
        return 
    
    
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.sum = 0
        self.depthSumHelper(nestedList, 1)
        return self.sum
 
    def depthSum_2(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.sum = 0
        stack = []
        for nestedInteger in nestedList:
            stack.append(nestedInteger)
        currentLevel = 1
        nextLevel = []
        while stack:
            nestedInteger = stack.pop(0)
            if nestedInteger.isInteger():
                self.sum += nestedInteger.getInteger()*currentLevel
            else:
                for nested in nestedInteger.getList():
                    nextLevel.append(nested)
            if not stack:
                stack = nextLevel
                nextLevel = []
                currentLevel += 1
        return self.sum        

    def depthSum_3(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if len(nestedList) == 0: return 0
        stack = []
        sum = 0
        for n in nestedList:
            stack.append((n, 1))
        while stack:
            next, d = stack.pop(0)
            if next.isInteger():
               sum += d * next.getInteger()
            else:
                for i in next.getList():
                    stack.append((i,d+1))
        return sum
