from collections import deque
class Solution(object):

    
    def __init__(self):
        self.nth = -1

    def traverse(self,x, y, height, width, grid ,distance):
        queue = deque([(x,y)])
        level = 1
        nth = self.nth 
        while queue :
            for _ in xrange(len(queue)):
                currentX, currentY = queue.popleft()
                for deltaX, deltaY in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    nextX, nextY = currentX + deltaX, currentY + deltaY
                    if 0 <= nextX < width and 0 <= nextY < height and grid[nextY][nextX] == nth + 1:
                        queue.append((nextX, nextY))
                        distance[nextY][nextX] += level
                        grid[nextY][nextX] =nth
            level += 1
        self.nth -= 1
    



    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height, width, self.nth = len(grid), len(grid[0]), -1
        distance = [[0] * width for _ in xrange(height)]
        buildingNum = len([self.traverse(x, y, height, width, grid,distance)\
                            for y , row in enumerate(grid) \
                            for x, col  in enumerate(row) if grid[y][x] == 1\
                            ])

        return min([
            distance[i][j]
            for i, row in enumerate(grid)
            for j, num in enumerate(row)
            if num == -buildingNum
        ] or [-1])

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])
