class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        width = len(matrix[0]) if matrix else 0
        height = len(matrix)
        self.data = [[0 for _ in xrange(0, width + 1)] for _ in xrange(0, height + 1)]
        for y in xrange(1, height+1):
            for x in xrange(1, width + 1):
                self.data[y][x] = self.data[y-1][x] + self.data[y][x-1] - self.data[y-1][x-1] + matrix[y-1][x-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.data[row2+1][col2+1] - self.data[row2+1][col1] - self.data[row1][col2+1] + self.data[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
