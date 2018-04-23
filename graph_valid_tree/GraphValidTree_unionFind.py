class Solution(object):
   
    def __init__(self):
        self.parents = []

    def find(self, x):
        return x if self.parents[x] == x else self.find(self.parents[x])

    def validTree(self, n, edges):
        self.parents = range(n)
        for edge in edges:
            p1, p2 = map(self.find,edge)
            if p1 == p2:
                return False
            self.parents[p2] = p1
        return len(edges) == n -1 
        
#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    print sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3]])
    print sol.validTree(4, [[0,1],[2,3],[1,2]])
    print sol.validTree(5, [[0,1],[1,2],[3,4]])
