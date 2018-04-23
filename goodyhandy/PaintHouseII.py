class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        preMin, preSecond, idx = 0, 0, None
        for i, cost in enumerate(costs):
            tempPreMin, tempPreSecond , tempIdx= float('inf'), float('inf'), -1
            for j, c in enumerate(cost):
                cost[j] += preMin if idx != j else preSecond
                if tempPreMin > cost[j] :
                    tempIdx =  j; tempPreSecond = tempPreMin ; tempPreMin = cost[j]
                elif tempPreSecond > cost[j]:
                    tempPreSecond = cost[j]
            preMin, preSecond, idx = tempPreMin, tempPreSecond, tempIdx
        return preMin
