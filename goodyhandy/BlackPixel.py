class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        #bfs to fuck it
        x, y = y, x
        width = len(image[0]); height = len(image)
        from collections import deque
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set([(x, y)])
        leftMost = x; rightMost = x
        upMost = y; downMost = y
        queue = deque()
        queue.append((x, y))
        while queue:
            currentX, currentY = queue.popleft()
            for dx, dy in directions :
                nextX, nextY = currentX + dx, currentY + dy
                if (nextX, nextY) not in visited and 0<=nextX<width and 0<=nextY <height and  image[nextY][nextX] == '1' :
                    visited.add((nextX, nextY))
                    leftMost = min(leftMost, nextX); rightMost = max(rightMost, nextX)
                    upMost = min(upMost, nextY); downMost = max(downMost, nextY)
                    queue.append((nextX, nextY))
        return (rightMost- leftMost + 1)*(downMost - upMost + 1)
