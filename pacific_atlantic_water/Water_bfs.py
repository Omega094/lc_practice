class Solution(object):
    def bfs(self,matrix, queue, visited):
        directions = [(1, 0),(-1, 0), (0, 1), (0, -1)]
        while queue:
            currentX, currentY = queue.pop(0)
            for dx, dy in directions:
                newX, newY = currentX + dx, currentY + dy
                if 0<= newX <self.width and 0<=newY < self.height and (newY, newX) not in visited and matrix[newY][newX] >= matrix[currentY][currentX]:
                    queue.append((newX, newY))
                    visited.add((newY, newX))
        return visited
        
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        width = len(matrix[0]);height = len(matrix); self.width = width; self.height = height
        pQueue = []; pSet = set(); aQueue = []; aSet = set()
        for x in xrange(width):
            for y in xrange(height):
                if y == 0 or x == 0:
                    pSet.add((y, x))
                    pQueue.append((x,y))
                if x == width-1 or y == height -1 :
                    aSet.add((y,x))
                    aQueue.append((x, y))
        return list(self.bfs(matrix, aQueue, aSet) & self.bfs(matrix,pQueue, pSet))
                
