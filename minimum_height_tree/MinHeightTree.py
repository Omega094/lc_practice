#This approach is correct, but it will be TLE. 
#We don't need to traverse each node and get their height.
#Just construct a graph and do topology sort. 
class Solution(object):

    def __init__(self):
        from collections import defaultdict
        self.graph = defaultdict(list)    
    
    def treeHeight(self, start):
        visited = set()
        height = 0
        queue = [start, -1]
        while not (len(queue) == 1 and queue[0] == -1):
            currentNode = queue.pop(0)
            if currentNode == -1: 
                height += 1
                queue.append(-1)
            visited.add(currentNode)
            #print queue
            for child in self.graph[currentNode]:
                if child not in visited:
                    queue.append(child)
        return height
        
        #use bfs to traverse and calculate the height
    
    def buildGraph(self, edges):
        from collections import defaultdict
        self.graph = defaultdict(list)
        for edge in edges:
            p1, p2 = edge[0], edge[1]
            self.graph[p1].append(p2)
            self.graph[p2].append(p1)
        return 
    
    
    
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.buildGraph(edges)
        nodeAndHeight = [(node, self.treeHeight(node)) for node in xrange(0, n)]
        nodeAndHeight.sort(key = lambda x : x[1])
        result = []
        if nodeAndHeight:
            smallestHeight = nodeAndHeight[0][1]
        while nodeAndHeight and nodeAndHeight[0][1] == smallestHeight:
            result.append(nodeAndHeight.pop(0)[0])
        return result

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
    print sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])



