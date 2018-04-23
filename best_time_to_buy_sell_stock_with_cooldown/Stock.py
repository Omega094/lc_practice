class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        length = len(prices)
        sell_profit = [0]*length
        buy_profit = [0] * length
        buy_profit[0] = -prices[0]
        for i in range(1, length):
            delta = prices[i] - prices[i-1]
            #This profit is either
            #1: We buy yesterday and sell it today. 
            #2: We move the sell from sell_profit[i-1] to today. 
            sell_profit[i] = max(buy_profit[i-1] + prices[i], sell_profit[i-1] + delta)
            #This profit is either:
            #1: We sell_profit[i-2] - prices[i]
            #2: We move the buy from yesterday to today. 
            buy_profit[i] = max(sell_profit[i-2] - prices[i], buy_profit[i-1]-delta) if i >=2 else -prices[i]
        return max(sell_profit)

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.maxProfit([1, 2, 3, 0, 2])
