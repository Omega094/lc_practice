class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]: return 0
        import heapq
        heap = []
        width = len(heightMap[0])
        height = len(heightMap)
        visited = set()
        for x in xrange(0, width):
            for y in xrange(0, height):
                if x == 0 or x == width -1 or y == 0 or y == height-1:
                    visited.add((x, y))
                    heapq.heappush(heap, (heightMap[y][x], x, y))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        water = 0
        while heap:
            currentHeight, currentX, currentY = heapq.heappop(heap)
            for dx, dy in directions:
                nextX, nextY = currentX + dx, currentY + dy
                if 0 <= nextX < width and 0 <= nextY < height and (nextX, nextY) not in visited:
                    nextHeight = heightMap[nextY][nextX]
                    water +=  max(0, currentHeight - nextHeight)
                    nextHeight = max(nextHeight, currentHeight)
                    heapq.heappush(heap,(nextHeight, nextX, nextY))
                    visited.add((nextX, nextY))
        return water
