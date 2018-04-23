class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        minPrice = prices[0]
        maxProfit = 0
        #KeepTrack of min price and max profit
        for i in range(1, len(prices)):
            maxProfit = max(prices[i] - minPrice, maxProfit)
            minPrice = min(prices[i], minPrice)
        return maxProfit


