#Same thought as topology sort
#Remove leaves level by level. (Leave means the nodes that has degree 1
#Also, the min num of MHT is 2, image if there are 3, then there would be one node we can
#remove, which makes it 2 

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        self.graph = defaultdict(list)
        for p1, p2 in edges:
            self.graph[p1].append(p2)
            self.graph[p2].append(p1)
        vertices = set(self.graph.keys())
        while len(vertices) > 2:
            leaves = [x for x in self.graph if len(self.graph[x]) == 1]
            for leaf in leaves:
                parent = self.graph[leaf][0]
                self.graph[parent].remove(leaf)
                del self.graph[leaf]
                vertices.remove(leaf)
        return list(vertices) if n != 1 else [0]

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
    print sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])

