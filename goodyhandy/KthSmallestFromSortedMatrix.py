class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap  = []
        import heapq
        for i in xrange(0, len(matrix)):
            heapq.heappush(heap, (matrix[i].pop(0), i))
        for i in xrange(k):
            currentVal, currentLine = heapq.heappop(heap)
            if i == k-1: return currentVal
            if matrix[currentLine]:
                heapq.heappush(heap, (matrix[currentLine].pop(0), currentLine))
        return 
