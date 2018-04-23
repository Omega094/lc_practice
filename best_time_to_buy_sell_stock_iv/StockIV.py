class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        if k >= len(prices) / 2:
            maxProfit = 0
            for i in xrange(1, len(prices)):
                maxProfit += max(prices[i] - prices[i-1],0)
            return maxProfit

        #This is a two dimension DP problem, we have two variables,
        #the day, and the transaction.  table[i][j] is ith day with j (at most) transactions.
        days = len(prices)
        #local_max[j][i] is The table that saves max profit if we make transaction close on day i for the j th transaction. 
        local_max  = [[0]*days for _ in xrange(0, k + 1)]
        #global_max[j][i] saves the mas profit at most j transactions at day i. 
        global_max = [[0]*days for _ in xrange(0, k + 1)]
        for day in xrange(1, days):
            delta = prices[day] - prices[day-1]
            for t in xrange(1, k+1):
                #We either make the transaction from yesterday to today,
                #Or just not closing transaction yesterday. 
                local_max[t][day] = max(global_max[t-1][day-1] + max(0, delta), local_max[t][day-1]+delta)
                #Global profit might or might not be affected by the local max
                global_max[t][day] = max(global_max[t][day-1], local_max[t][day])
        return global_max[k][-1]

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.maxProfit(2, [3,2,6,5,0,3])
