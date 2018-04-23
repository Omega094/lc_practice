class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        height = len(dungeon)
        width = len(dungeon[0])
        HP_Table = [[None for _ in xrange(width)] for _ in xrange(height)]
        HP_Table[height-1][width-1] = max(-dungeon[height-1][width-1], 0) + 1
        for y in range(height-1, -1, -1):
            for x in range(width-1, -1, -1):
                if x == width -1 and y == height - 1: continue
                if x != width-1 and y != height -1 :
                    min_hp_to_continue = min(HP_Table[y+1][x],HP_Table[y][x+1] )
                elif x == width - 1:
                    min_hp_to_continue = HP_Table[y+1][x]
                elif y == height - 1:
                    min_hp_to_continue = HP_Table[y][x+1]
                HP_Table[y][x] = max(min_hp_to_continue - dungeon[y][x], 1)
        return HP_Table[0][0]


#test:
if __name__ == "__main__":
    dungeon = [[-2,-3,3],[-5, -10, 1], [10, 30, -5]]
    sol = Solution()
    print sol.calculateMinimumHP(dungeon)
