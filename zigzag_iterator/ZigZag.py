class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.x = 0
        self.y = 0
        if len(v1) > len(v2):
            v2 +=[None]* (len(v1) - len(v2))
        if len(v2) > len(v1):
            v1 +=[None]* (len(v2) - len(v1))
        self.data = [v1, v2]
        self.nextNotNone()
    
    def nextNotNone(self):
        if not self.hasNext(): return 
        while self.x < len(self.data[0]) and self.data[self.y][self.x] == None:
            self.y = (self.y + 1) % 2
            if self.y % 2 == 0:
                self.x += 1
        return 

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext(): return
        val = self.data[self.y][self.x]
        self.y = (self.y + 1) % 2
        if self.y % 2 == 0:
            self.x += 1
        self.nextNotNone()
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.x < len(self.data[0])
        
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
