from collections import defaultdict, deque

class Solution(object):
    
    def buildGraph(self, tickets):
        graph = defaultdict(list)
        for s, d, in tickets:
            graph[s].append(d)
        for s in graph.keys():
            graph[s].sort()
            graph[s] = deque(graph[s])
        return graph
        
    def dfs(self, graph, source, targetLen, path):
        path.append(source)
        if len(path) == targetLen:
            return True
        for _ in xrange(len(graph[source])):
            t = graph[source].popleft()
            if self.dfs(graph, t, targetLen, path):
                return True
            graph[source].append(t)
        path.pop()
        return False
            
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = self.buildGraph(tickets)
        path = []; source = "JFK"; targetLen = len(tickets) + 1
        self.dfs(graph, source, targetLen, path)
        return path
