class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        dp1 = [0 for _ in range(0, len(prices))]
        highestPrice = prices[-1]
        maxPrice = prices[-1]
        for i in range (len(prices)-2, -1, -1):
            dp1[i] = max(highestPrice - prices[i],  0)
            highestPrice = max(highestPrice, prices[i])
        maxProfitFromStart = 0
        maxTotalProfit = dp1[0]
        lowestPrice = prices[0]
        for i in range(1, len(prices)):
            maxProfitFromStart = max(maxProfitFromStart , prices[i] - lowestPrice)
            maxTotalProfit = max(maxProfitFromStart+dp1[i], maxTotalProfit)
            lowestPrice = min(lowestPrice, prices[i])
        return maxTotalProfit



#test
if __name__ == "__main__":
    prices = [1,2,4]
    prices2 = [2,1,2,0,1]
    sol = Solution()
    print sol.maxProfit(prices)
    print sol.maxProfit(prices2)
