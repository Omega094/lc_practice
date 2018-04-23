 
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        if not grid or not grid[0]:
            return result
        height = len(grid)
        width = len(grid[0])
        down = [[0 for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
        right = [[0 for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
        for y in xrange(height-1, -1, -1):
            for x in xrange(width-1, -1, -1):
                if grid[y][x] == "W":
                    down[y][x] = 0; right[y][x] = 0
                else:
                    check = int(grid[y][x] == "E")
                    if y == height -1:   
                        down[y][x] = check
                    else:
                        down[y][x] = down[y+1][x] + check
                    if x == width - 1:
                        right[y][x] = check
                    else:
                        right[y][x] = right[y][x+1] + check
        left = 0
        result = 0
        up = [0 for _ in xrange(width)]
        for y in xrange(height):
            left = 0
            for x in xrange(width):
                if grid[y][x] == "E":
                        left += 1; up[x] = up[x] + 1
                elif grid[y][x] == "W":
                    left = 0; up[x] = 0
                else:
                    result = max(result , down[y][x] + right[y][x] + left + up[x])
        #print down, right, up
        return result 

