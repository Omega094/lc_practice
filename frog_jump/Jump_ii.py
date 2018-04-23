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
        
        q = collections.deque()
        q.append((0,0))
        stoneSet = set(stones)
        while q:
            s , step = q.popleft()
            if s  == stones[-1]: return True
            for nextStep in (step-1, step, step+1):
                if nextStep > 0 and s + nextStep in stoneSet and not mapToTable[s + nextStep][nextStep] :
                    mapToTable[s + nextStep][nextStep] = True
                    q.append((s + nextStep, nextStep))
        #print dp
        return False
