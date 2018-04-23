from collections import deque

class Solution(object):
    def bfs(self, y, x, grid, distanceMatrix, visited):
        queue = [(x, y)]
        distance = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            nextLevel = []
            distance += 1
            for x, y in queue:
                for dx, dy in directions :
                    newX, newY = x + dx, y + dy
                    if 0<= newX <self.width and 0<=newY < self.height and (newX, newY) not in visited and grid[newY][newX] == 0:
                        nextLevel.append((newX, newY))
                        distanceMatrix[newY][newX][0] += distance
                        distanceMatrix[newY][newX][1] += 1
                        visited.add((newX, newY))
            queue = nextLevel
        return

    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.width = len(grid[0])
        self.height = len(grid)
        distanceMatrix = [[[0,0] if grid[y][x] not in (1, 2) else (float('inf'),0) for x in xrange(self.width) ] for y in xrange(self.height)]
        count = 0
        for x in xrange(0, self.width):
            for y in xrange(0, self.height):
                if grid[y][x] == 1:
                    self.bfs(y, x, grid, distanceMatrix, set())
                    count += 1
        minDist = float('inf')
        for x in xrange(0, self.width):
            for y in xrange(0, self.height):
                if distanceMatrix[y][x][1] == count:
                    minDist = min(minDist, distanceMatrix[y][x][0])
        return minDist if minDist != float('inf')  else -1
        
