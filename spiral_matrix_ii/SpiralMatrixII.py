class Solution(object):

    def generateMatrix(self, n):
        matrix = [ [ None for _ in xrange(n) ] for _ in xrange(n) ]
        upBound = 0; leftBound = 0;
        downBound = n-1; rightBound = n-1
        RIGHT = 0; DOWN = 1; LEFT = 2; UP = 3
        DIRECTION = 0
        counter = 1
        while True :
            if DIRECTION == RIGHT:
                for i in range (leftBound, rightBound+1):
                    matrix[upBound][i] = counter
                    counter += 1
                upBound += 1
            if DIRECTION == DOWN:
                for i in range (upBound, downBound+1):
                    matrix[i][rightBound] = counter
                    counter += 1
                rightBound -= 1
            if DIRECTION == LEFT:
                for i in range (rightBound, leftBound-1, -1):
                    matrix[downBound][i] = counter
                    counter += 1
                downBound -= 1
            if DIRECTION == UP:
                for i in range (downBound, upBound-1, -1):
                    matrix[i][leftBound] = counter
                    counter += 1
                leftBound += 1
            if leftBound > rightBound or upBound > downBound: return matrix
            DIRECTION = (DIRECTION + 1) % 4


#test 
if __name__ == "__main__":
    sol = Solution()
    print sol.generateMatrix(3)
