class Union(object):
    
    def __init__(self):
        self.id = {}
        self.count = 0
    
    def add(self, p):
        self.id[p] = p
        self.count += 1
    
    def findRoot(self, p):
        while p != self.id[p]:
            #find to the upper level
            self.id[p] = self.id[self.id[p]]
            #compress
            p = self.id[p]
        return p
    
    def unite(self, p, q):
        i, j = self.findRoot(p), self.findRoot(q)
        if i == j:
            return
        self.id[i] = j
        self.count -= 1
    
    
        
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        solution = []
        islands = Union()
        for p in map(tuple, positions):
            islands.add(p)
            for direction in (0,1), (0, -1), (1,0), (-1,0):
                q = (p[0] + direction[0], p[1] + direction[1])
                if q in islands.id:
                    islands.unite(p, q)
            solution.append(islands.count)
            #print islands.id, islands.size
        return solution
        

