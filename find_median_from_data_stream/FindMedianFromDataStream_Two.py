from heapq import *
 
class MedianFinder:
    def __init__(self):
        self._small = []
        self._large = []

    def addNum(self, num):
        if len(self._large) == len(self._small):
            heappush(self._small, -num)
            smallTop = -heappop(self._small)
            heappush(self._large, smallTop)
        else:
            heappush(self._large, num)
            largeTop = heappop(self._large)
            heappush(self._small, -largeTop)

    def findMedian(self):
        if (len(self._large) + len(self._small)) % 2 == 0:
            return  (-float(self._small[0]) + float(self._large[0])) / 2
        return float(self._large[0])

        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()