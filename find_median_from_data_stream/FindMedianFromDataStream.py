from heapq import *
class MedianFinder(object):

    def __init__(self):
        self._maxHeap = []
        self._minHeap = []

    def addNum(self, num):
        heapq.heappush(self._maxHeap, -num)
        #First we need to guarantee that minHead top is larger than maxHeap top
        minTop = self._minHeap[0] if self._minHeap else None
        maxTop = -self._maxHeap[0] if self._maxHeap else None

        while maxTop > minTop or len(self._minHeap) < len(self._maxHeap) - 1:
            heapq.heappush(self._minHeap, -heapq.heappop(self._maxHeap))
            minTop = self._minHeap[0] if self._minHeap else None
            maxTop = -self._maxHeap[0] if self._maxHeap else None
        while len(self._minHeap) > len(self._maxHeap):
            heapq.heappush(self._maxHeap, -heapq.heappop(self._minHeap))

    def findMedian(self):
        if len(self._minHeap) == len(self._maxHeap):
            return (self._minHeap[0] + (-self._maxHeap[0]))/2.0
        else:
            return -1.0*self._maxHeap[0]

