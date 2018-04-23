class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix: return 
        self.matrix = matrix
        self.row = len(matrix[0]) + 1
        self.col = len(matrix) + 1
        self.bit = [[0 for _ in xrange(self.row)] for _ in xrange(self.col)]
        for i in xrange(len(self.matrix)):
            for j in xrange(len(self.matrix[0])):
                self.add(i, j , matrix[i][j])
        return

    def update(self, row, col, val):
        delta = val - self.matrix[row][col]
        if delta != 0:
            self.add(row, col, delta)
            self.matrix[row][col] = val
        return 

    def sumRegion(self, row1, col1, row2, col2):

        def sumRegion_bit(row, col):
            row = row + 1
            col = col + 1
            i = row
            ret = 0
            while i > 0:
                j = col
                while j > 0 :
                    ret += self.bit[i][j]
                    j -= (j & -j)
                i -= (i & -i)
            return ret

        ret = sumRegion_bit(row2, col2)
        if row1 > 0 and col1 > 0:
            ret += sumRegion_bit(row1 - 1, col1 -1)
        if col1 > 0:
            ret -= sumRegion_bit(row2, col1 - 1)
        if row1 > 0:
            ret -= sumRegion_bit(row1 - 1, col2)
        return ret

    def add(self, row, col, val):
        row = row + 1
        col = col + 1
        i = row
        while i < self.col :
            j = col
            while j < self.row:
                self.bit[i][j] += val
                j += (j & -j)
            i += (i & -i)
        return

