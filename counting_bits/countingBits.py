class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for x in range(1, num + 1):
            ans += ans[x & (x - 1)] + 1,
        return ans

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.countBits(5201314)
