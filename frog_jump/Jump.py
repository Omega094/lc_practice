class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp = []
        mapToTable = {}
        cm = stones[0]
        for i in xrange(0, len(stones)):
            if stones[i] > cm : return False
            dp.append([False]*(i+1))
            cm = cm + (i+1)
            mapToTable[stones[i]] = dp[i]
            
        dp[0][0] = True
        for i, s in enumerate(stones):
             for j in xrange(len(dp[i])):
                if dp[i][j] == True:
                    for val in [s+j, s+j-1, s+j+1]:
                        #print val, s, j
                        if val in mapToTable and val > s:
                             mapToTable[val][val - s] = True
        #print dp
        return True in mapToTable[stones[-1]]
