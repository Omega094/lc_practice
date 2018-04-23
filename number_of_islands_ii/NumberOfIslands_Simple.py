class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        self.parents = {}
        self.count = 0
        solution = []
        
        def add(p):
            self.parents[p] = p
            self.count += 1
        
        def findRoot(p):
            temp = p
            #Keep finding ancestor
            while self.parents[p] != p:
                self.parents[p] = self.parents[self.parents[p]]
                p = self.parents[p]
            self.parents[temp] = p #Compress here !
            return p
        
        def unite(p, q):
            i, j = findRoot(p), findRoot(q)
            if i == j:
                return
            self.parents[i] = j
            self.count -= 1
        
        for p in map(tuple, positions):
            add(p)
            for direction in (0,1), (0, -1), (1,0), (-1,0):
                q = (p[0] + direction[0], p[1] + direction[1])
                if q in self.parents:
                    unite(p, q)
            solution.append(self.count)
        return solution

