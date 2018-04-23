class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        #Remember how to use comparator 
        envelopes.sort( cmp = lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        dp = []
        for width, height in envelopes:
            start = 0 
            end = len(dp) - 1
            while start <= end :
                mid = (start + end) // 2
                if dp[mid] < height :
                    start = mid + 1
                else:
                    end = mid - 1
            if start >= len(dp):
                dp.append(height)
            else:
                dp[start] = height
        #print envelopes
        return len(dp)
        
#test
sol = Solution()
print sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])
