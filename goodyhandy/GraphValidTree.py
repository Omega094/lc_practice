class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        parents = {i : i for i in xrange(n)}
        
        def find(node):
            parent = parents[node]
            if parent == node:
                return parent
            parents[node] = parent
            return find(parent)
        
        for n1, n2 in edges:
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            parents[p1] = p2
        return len(edges) == n-1

#test
sol = Solution()
print sol.validTree([[0,1],[0,2],[0,3],[1,4]])
