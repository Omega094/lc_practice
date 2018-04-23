#First find the median point 
#Then calculate the total distance
#Since it is manhattan distance
#So we can jusst add
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        width = len(grid[0])
        height = len(grid)
        horizontalDists = [ x for x in xrange(0, width) for y in xrange(0, height) if grid[y][x] == 1]
        verticalDists = [ y for y in xrange(0, height) for x in xrange(0, width) if grid[y][x] == 1]
        horizontalDists.sort()
        verticalDists.sort()
        #Median !!! not average !!!
        midHorizontal = horizontalDists[len(horizontalDists)/2]
        midVertical = verticalDists[len(verticalDists)/2]
        return sum(map(lambda x : abs(x - midHorizontal), horizontalDists)) + sum(map(lambda y : abs(y - midVertical), verticalDists))

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]])
