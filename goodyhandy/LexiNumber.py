class Solution(object):
    def dfs(self, base, solution, limit):
        if base > limit:
            return
        solution.append(base)
        if base*10 > limit: return 
        for i in xrange(0, 10):
            if base*10+i > limit: 
                break
            self.dfs(base*10 + i, solution,limit)
        return 

    def lexicalOrder(self,n):
        solution = []
        for i in xrange(1, 10):
            self.dfs(i, solution, n)
        return solution
#test
sol = Solution()
print sol.lexicalOrder(14)
