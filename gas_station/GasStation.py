class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost): return -1
        #sum is current total gas. 
        total = 0
        #diff is sum + gas[i] - cost[i]
        diff = 0
        k = 0
        for i in range(0, len(gas)):
            total = total + gas[i]
            total = total - cost[i]
            if total  < 0:
                total = 0
                k = i + 1
                print k, "This is k"
        return k if k < len(gas) else -1
