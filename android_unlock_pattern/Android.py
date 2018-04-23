class Solution(object):
    
    def dfs(self, visited, currentSequence, count):
        if len(currentSequence)>= self.n: return count+1
        if len(currentSequence)>= self.m : count += 1
        for i in xrange(1, 10):
            sortedTuple = tuple(sorted([currentSequence[-1], i]))
            if i not in visited and (not currentSequence or sortedTuple not in self.jump or self.jump[sortedTuple] in visited):
                visited.add(i)
                currentSequence.append(i)
                count = self.dfs(visited, currentSequence, count)
                visited.remove(i)
                currentSequence.pop()
        return count
        
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.m = m; self.n = n
        self.count = 0
        self.jump = {(1,3): 2, (4,6): 5, (7,9): 8, (1,7):4, (2,8):5, (3,9):6, (1,9): 5, (3, 7): 5}
        result = 0
        result += 4*self.dfs(set([1]), [1], 0)
        result += 4*self.dfs(set([4]), [4], 0)
        result += self.dfs(set([5]),[5], 0)
        return result 
        

