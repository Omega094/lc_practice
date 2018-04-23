class Solution(object):
    
    def updateGraph(self, node,graph,visitedSet, valMap, scale):
        visitedSet.add(node)
        valMap[node] *= scale
        for c in graph[node]:
            if c not in visitedSet:
                self.updateGraph(c,graph,visitedSet, valMap, scale)
        return 
    def sameGraph(self, s, t, graph, visited):
        visited.add(s)
        if t in graph[s]: return True
        for c in graph[s]:
            if c not in visited:
                if self.sameGraph(c, t, graph, visited): return True
        return False
        
    def calcEquation(self, equations, values, query):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type query: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        valMap = {}
        graph = defaultdict(set)
        values = map(float, values)
        for i, (a, b) in enumerate(equations):
            if a not in valMap and b not in valMap:
                valMap[b] = 1.0
                valMap[a] = values[i]
            elif a not in valMap:
                valMap[a] = valMap[b]*values[i]
            elif b not in valMap:
                valMap[b] = valMap[a]/values[i]
            else:
                if valMap[a]/valMap[b] != values[i]: 
                    scale = valMap[a]/values[i]/valMap[b]
                    self.updateGraph(b, graph, set(), valMap, scale)
            graph[a].add(b)
            graph[b].add(a)
        result = []
        
        for a, b in query:
            if a not in valMap or b not in valMap:
                result.append(-1.0)
                continue
            if self.sameGraph(a, b, graph, set()):
                result.append(valMap[a]/valMap[b])
            else: 
                result.append(-1.0)
        return result
