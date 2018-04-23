class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        startX = len(matrix[0])-1
        startY = 0
        while startX!= -1 and startY != len(matrix):
            if matrix[startY][startX] == target: return True
            if target > matrix[startY][startX] : startY += 1
            else: startX -= 1
        return False 
