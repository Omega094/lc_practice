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
        
        def find(p):
            parent = self.parents[p]
            if parent == p:
                return p
            self.parents[p] = parent
            return find(parent)
            
        def union(p, q):
            pP = find(p)
            pQ = find(q)
            #In this case we don't decrement count if they have same ancestors
            if pP == pQ: return 
            self.parents[pP] = pQ
            self.count -= 1
            return
        
        positions = map(tuple, positions)
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        for p in positions:
            add(p)
            for dx, dy in directions:
                parentPos = (p[0] + dx, p[1] + dy)
                if parentPos in self.parents:
                    union(p, parentPos)
            solution.append(self.count)
        return solution
