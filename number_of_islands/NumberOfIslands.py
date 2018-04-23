class Solution(object):
    
    def __init__(self):
        self.counter = 0

    def dfsHelper(self, grid,x, y):
        if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
            if grid[y][x] == '1':
                grid[y][x]=  'D' 
                self.dfsHelper(grid, x-1, y)
                self.dfsHelper(grid, x+1, y)
                self.dfsHelper(grid, x, y+1)
                self.dfsHelper(grid, x, y-1)
            return 

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        self.counter = 0
        height = len(grid)
        width = len(grid[0])
        for i in range(0, height):
            for j in range(0, width):
                if grid[i][j] == "1":
                    self.counter += 1
                self.dfsHelper(grid, j, i)
        return self.counter

#test:
if __name__ == "__main__":
    sol = Solution()
    ocean = [["1","1","1"], ["1","1","0"],["1","0","1"]]
    print ocean
    print sol.numIslands(ocean)
    print ocean

