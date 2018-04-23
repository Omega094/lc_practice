class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        from collections import deque
        queue = deque([(x, y) for y, row in enumerate(rooms) for x , point in enumerate(row) if point == 0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        while queue:
            currentX, currentY = queue.popleft()
            for dx, dy in directions:
                nextX, nextY = currentX + dx , currentY + dy
                if nextX >= 0 and nextY >= 0 and nextX < len(rooms[0]) and nextY < len(rooms) and rooms[nextY][nextX] == INF:
                    rooms[nextY][nextX] = rooms[currentY][currentX] + 1
                    queue.append((nextX, nextY))
        return
