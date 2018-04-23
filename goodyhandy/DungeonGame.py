class Solution(object):
    def calculateMinimumHP(self, d):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        width = len(d[0])
        height = len(d)
        hp_min = [[0 for _ in xrange(len(d[0]))] for _ in xrange(len(d))]
        hp_min[height-1][width -1] = max(-d[-1][-1], 0 ) + 1
        for y in xrange(height-1, -1, -1 ):
            for x in xrange(width-1, -1, -1):
                if y == height-1 and x == width-1 : continue 
                if y == height - 1:
                    min_hp_exit = hp_min[y][x+1]
                elif x == width - 1:
                    min_hp_exit = hp_min[y+1][x]
                else:
                    min_hp_exit = min(hp_min[y+1][x], hp_min[y][x+1])
                hp_min[y][x] = max(min_hp_exit - d[y][x], 1)
        return hp_min[0][0]
