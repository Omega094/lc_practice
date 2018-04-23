class Solution(object):
    
    def find(self, x):
        if self.parent[x] != x:
            parent = self.find(self.parent[x])
            self.parent[x] = parent
            return parent
        else:
            return x

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.parent = {i: i for i in xrange(n)}
        for x, y in edges:
            xParent, yParent = self.find(x), self.find(y)
            #Only union their parents
            self.parent[yParent] = xParent
        #Union all parents. (Compress again)
        parents = map(self.find, self.parent.values())
        return len(set(parents))
