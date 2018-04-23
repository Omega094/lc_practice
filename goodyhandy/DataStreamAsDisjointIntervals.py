# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        heapq.heappush(self.data, (val, Interval(val, val)))
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        result = []
        currentVal , currentInterval = heapq.heappop(self.data)
        while self.data:
            nextVal, nextInterval = heapq.heappop(self.data)
            if currentInterval.end >= nextInterval.start-1:
                currentInterval.end = max(currentInterval.end, nextInterval.end)
            else:
                result.append((currentVal, currentInterval))
                currentVal, currentInterval = nextVal, nextInterval
        result.append((currentVal, currentInterval))
        self.data = result
        return map(lambda x :x[1], result)
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
