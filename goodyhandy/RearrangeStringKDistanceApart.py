import heapq
from collections import  Counter, deque
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        charCounter = Counter(str)
        heap = [(-charCounter[c], c) for c in charCounter]
        heapq.heapify(heap)
        result = []
        if k == 0: return str
        while heap:
            temp = deque()
            for i in xrange(min(k, len(heap))):
                temp.append(heapq.heappop(heap))
            #This means the one with most freq will never be made k distance apart. 
            if len(temp) < k and temp[0][0]<-1 : return ""
            nextTemp = []
            for freq, char in temp:
                result.append(char)
                freq += 1
                if freq != 0:
                    heapq.heappush(heap, (freq, char))
        return "".join(result)
