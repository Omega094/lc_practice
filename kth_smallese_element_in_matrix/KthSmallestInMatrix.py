class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = [(row[0], i, 0) for i, row in enumerate(matrix) ]
        heapq.heapify(heap)
        for _ in xrange(k-1):
            currentVal, rowNum, col = heapq.heappop(heap)
            if col + 1< len(matrix[0]):
                heapq.heappush(heap, (matrix[rowNum][col + 1], rowNum, col+1))
        return heap[0][0]
