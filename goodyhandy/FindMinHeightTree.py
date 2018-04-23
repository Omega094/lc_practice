class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        graph = defaultdict(set)
        degree = defaultdict(int)
        for p1, p2 in edges:
            graph[p1].add(p2)
            graph[p2].add(p1)
            degree[p1] += 1
            degree[p2] += 1
        vertices = set(range(n))
        queue  = deque()
        for p in degree:
            if degree[p] == 1:
                queue.append(p)
        while queue and len(vertices) > 2:
            nextQueue = deque()
            for current in queue:
                del degree[current]
                vertices.remove(current)
                for child in graph[current]:
                    graph[child].remove(current)
                    degree[child] -= 1
                    if degree[child] == 1:
                        nextQueue.append(child)
            queue = nextQueue
        return list(vertices)
