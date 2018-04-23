class Solution(object):
    def buildGraph(self, edges):
        from collections import defaultdict
        self.graph = defaultdict(set)
        for p1, p2 in edges:
            if p1 > p2:
                p1, p2 = p2, p1
            self.graph[p1].add(p2)
    
    def validTree(self, n, edges):
        queue = []
        queue.append(0)
        self.buildGraph(edges)
        traversed = set()
        while queue:
            current = queue.pop(0)
            if current in traversed:
                return False
            traversed.add(current)
            for i in self.graph[current]:
                queue.append(i)
        return len(traversed) == n

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    print sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3]])
    print sol.validTree(4, [[0,1],[2,3],[1,2]])
    print sol.validTree(5, [[0,1],[1,2],[3,4]])
