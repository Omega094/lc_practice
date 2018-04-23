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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.lst = []
        self.counter = -1
        def dfsHelper(nestedList):
            for nested in nestedList:
                if nested.isInteger():
                    self.lst.append(nested.getInteger())
                else:
                    dfsHelper(nested.getList())
        dfsHelper(nestedList)
        #print self.lst, "This is self.lst"
        self.iterator = iter(self.lst) 

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext(): return 
        self.counter += 1
        #print self.lst
        return self.lst[self.counter]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.counter < len(self.lst) - 1
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
