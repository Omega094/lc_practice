class TreeNode(object):

    def __init__(self, val):
        self.neighbor = [None,None,None,None]
        self.leftTop = (0,0)
        self.rightBottom = (0, 0)
        self.val = val

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.nums = matrix
        if not matrix: return 
        if not matrix[0] : return 
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.root = self.createTree(matrix, (0, 0), (self.row - 1, self.col -1))
        

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[row][col]
        if diff == 0: return
        self.nums[row][col] = val
        self.updateTree(row, col, diff, self.root)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        currentVal = 0
        if self.root:
            return self.sumTreeRegion(row1, col1, row2, col2, self.root, 0)
        return 
        
    def createTree(self, matrix, start, end):
 
        if start[0] > end[0] or start[1] > end[1] or end[0] >=self.col or end[1] >= self.row:
            return
        root = TreeNode(0)
        root.leftTop = start
        root.rightBottom = end
        print start, end
        if start == end:
            root.val = matrix[start[0]][start[1]]
            return root
        midX = (start[0] + end[0]) / 2
        midY = (start[1] + end[1]) / 2
        root.neighbor[0] = self.createTree(matrix, start, (midX, midY))
        root.neighbor[1] = self.createTree(matrix, (start[0], midY +1), (midX, end[1]))
        root.neighbor[2] = self.createTree(matrix, (midX+1, start[1]), (end[1], midY))
        root.neighbor[3] = self.createTree(matrix, (midX+1, midY+1), end)
 
        for child in root.neighbor:
            if child :
                root.val += child.val
        return root

    def sumTreeRegion(self, row1, col1, row2, col2, root, currentVal ):
        start = root.leftTop
        end = root.rightBottom
        top = max(start[0], row1)
        bottom = min(end[0], row2)
        if bottom < top: return 0
        left = max(start[1], col1)
        right = min(end[1], col2)
        if left > right : return 0
        if row1 <= start[0] and col1 <= start[1] and row2 >= end[0] and col2 >= end[1] :
            return currentVal + root.val
        newVal = currentVal
        for i in xrange(0, 4):
            if root.neighbor[i]:
                newVal += self.sumTreeRegion(row1, col1, row2, col2, root.neighbor[i], currentVal)
        return newVal

    def updateTree(self, row, col, diff, root):
        if not root: return 
        if row >= root.leftTop[0] and row <= root.rightBottom[0] and col >= root.leftTop[1] and col <= root.rightBottom[1]:
            root.val += diff
            for i in xrange(0, 4):
                if root.neighbor[i]:
                    self.updateTree(row, col, diff, root.neighbor[i])

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)
 