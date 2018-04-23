import heapq
from collections import  Counter, deque
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k == 0: return s
        ctr = Counter(s)
        result = []
        heap = [(-count, c) for c, count in ctr.iteritems()]
        heapq.heapify(heap)
        while heap:
            current = []
            #This is important
            for i in xrange(min(len(s) - len(result), k)):
                #This means we don't have enough to build the string 
                if not heap: return ""
                current.append(heapq.heappop(heap))
            for freq, c in current:
                result.append(c)
                freq += 1
                if freq == 0: continue
                heapq.heappush(heap, (freq, c))
        return "".join(result)

#test
sol = Solution()
print sol.rearrangeString("aabbcc", 3)


                
