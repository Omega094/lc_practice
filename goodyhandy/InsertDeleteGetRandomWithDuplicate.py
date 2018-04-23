class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.dataList = []
        self.dataDict = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        notContain = True
        if self.dataDict.has_key(val): notContain = False
        self.dataList.append(val)
        idx = len(self.dataList) - 1
        self.dataDict[val].add(idx)
        return notContain
        
        
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        contain = self.dataDict.has_key(val)
        if not contain : return contain
        tailVal, tailValIdx, valIdx = self.dataList[-1], len(self.dataList)-1, self.dataDict[val].pop()
        #Swap
        self.dataList[valIdx], self.dataList[tailValIdx] = tailVal, val
        #Update dict
        if valIdx != tailValIdx:
            self.dataDict[tailVal].remove(tailValIdx)
            self.dataDict[tailVal].add(valIdx)
        self.dataList.pop()
        if len(self.dataDict[val]) == 0: del self.dataDict[val]
        return contain
        
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return self.dataList[random.randint(0, len(self.dataList) - 1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
