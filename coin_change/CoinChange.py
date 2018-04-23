class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        coinSet = set(coins)
        if amount in coinSet:
            return 1
        if amount < min(coins):
            return -1
        result = float('inf')
        for num in coins:
            coinNeeded = self.coinChange(coins, amount - num)
            if coinNeeded != -1:
                result = min(result, coinNeeded) + 1
        return result if result != float('inf') else  -1 


    def coinChange_2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        table = [0] + [float('inf')]*amount
        for i in xrange(1, amount+1):
            #This is the DP rule 
            table[i] = min(table[i-num]+1 if i - num >= 0 else float('inf') for num in coins)
        return [-1, table[-1] ][table[-1] != float('inf')]

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.coinChange([1,2,5], 100)
