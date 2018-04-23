class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        k = len(costs[0])
        prev = [0] * k
        for now in costs:
            temp = prev[:]
            for i in range(0, k):
                prev[i] = now[i] + (min(temp[:i] + temp[i+1:]) if len(temp) > 1 else 0)
        return min(prev)
