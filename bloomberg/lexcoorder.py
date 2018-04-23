class Solution(object):
    def lexicoOrder(self,n):
        return sorted(map(str, range(n)))
sol = Solution()
print sol.lexicoOrder(15)
