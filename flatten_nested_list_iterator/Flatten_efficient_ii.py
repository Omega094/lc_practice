class NestedIterator(object):

    def __init__(self, nestedList):
        self.queue = nestedList[:]

    def next(self):
        if not self.hasNext(): return 
        return self.queue.pop(0).getInteger()

    def hasNext(self):
        while self.queue and not self.queue[0].isInteger():
            self.queue  = self.queue.pop(0).getList() + self.queue
        if not self.queue:
            return False
        return True
        
