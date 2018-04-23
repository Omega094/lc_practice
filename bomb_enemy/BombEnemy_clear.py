class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        rowHitLeft = [[0 for i in xrange(len(grid[0]) )] for j in xrange(len(grid))]
        for i in range(0, len(grid)):
            count = 0
            for j in range(0, len(grid[0])):
                if grid[i][j] == "E":
                    count += 1
                    rowHitLeft[i][j] = count
                elif grid[i][j] == "0":
                    rowHitLeft[i][j] = count
                else:
                    count = 0
            count = 0
            for j in range(len(grid[0])-1, -1 , -1):
                if grid[i][j] == "E":
                    count += 1
                    rowHitLeft[i][j] += count
                elif grid[i][j] == "0":
                    rowHitLeft[i][j] += count
                else:
                    count = 0
                #print rowHitRight, "out"
        maxEnemy = 0
        for i in range(0, len(grid[0])):
            count = 0
            for j in range(0, len(grid)):
                if grid[j][i] == "E":
                    count += 1
                    rowHitLeft[j][i] += count
                elif grid[j][i] == "0":
                    rowHitLeft[j][i] += count
                else:
                    count = 0
            count = 0
            for j in range(len(grid) -1 , -1, -1):
                if grid[j][i] == "E":
                    count += 1
                    rowHitLeft[j][i] += count
                elif grid[j][i] == "0":
                    rowHitLeft[j][i] += count
                    maxEnemy = max(maxEnemy , rowHitLeft[j][i]  )
                else:
                    count = 0
        return maxEnemy

                    
                    
