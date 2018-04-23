class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.counter = 0
        self.sum = 0
        self.size = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.counter += 1
        if self.counter >= self.size:
            self.counter = 1
            self.sum = val 
            return val
        self.sum += val
        return self.sum/self.counter
        


