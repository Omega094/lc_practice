class Solution(object):
    
    def find(self, x):
        return x if self.parents[x] == x else self.find(self.parents[x])
    
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.parents = range(n)
        for edge in edges:
            p1, p2 = map(self.find, edge)
            self.parents[p2] = p1
        self.parents = map(self.find, self.parents)
        return len(set(self.parents))
        
#test
if __name__ == "__main__":
    sol = Solution()
    print sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
    print sol.countComponents(5, [[0, 1], [1, 2], [3, 4]])
