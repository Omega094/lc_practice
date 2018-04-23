class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        horizontal = [x for x in xrange(0, len(grid[0])) for y in xrange(0, len(grid)) if grid[y][x] ==1 ]
        vertical = [y for x in xrange(0, len(grid[0])) for y in xrange(0, len(grid)) if grid[y][x] ==1 ]
        horizontal.sort()
        vertical.sort()
        midH = horizontal[len(horizontal)/2]
        midV = vertical[len(vertical)/2]
        return sum(map(lambda x : abs(x - midH), horizontal)) + sum(map(lambda y : abs(y - midV), vertical)) 
