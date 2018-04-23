class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        arr = triangle[0]
        for i in xrange(1, len(triangle)):
            currentRow = triangle[i]
            for j in xrange(0, i + 1):
                if j == 0:
                    currentRow[j] += arr[0]
                elif j == i:
                    currentRow[i] += arr[-1]
                else:
                    currentRow[j] += min(arr[j], arr[j-1])
            arr = currentRow
        return min(arr)
        
