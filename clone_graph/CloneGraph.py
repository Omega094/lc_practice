class Solution(object):
    
    def dfsCopy(self, node, newNode, visited):
        if node.label in visited: return 
        visited[node.label] = newNode
        for child in node.neighbors:
            if child.label not in visited:
                newChild = UndirectedGraphNode(child.label)
            else:
                newChild = visited[child.label]
            newNode.neighbors.append(newChild)
            self.dfsCopy(child, newChild, visited)
        return 

    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        visited = dict()
        if not node : return None
        resultNode = UndirectedGraphNode(node.label)
        self.dfsCopy(node, resultNode, visited)
        return resultNode


    def cloneGraph_bfs(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node: return None
        visited = set()
        queue = []
        resultQueue = []
        queue.append(node)
        solutionNode = UndirectedGraphNode(node.label)
        currentNode = solutionNode
        resultQueue.append(solutionNode)
        while queue:
            originNode = queue.pop(0)
            resultNode = resultQueue.pop(0)
            if originNode.label not in visited:
                visited.add(originNode.label)
                for node in originNode.neighbors:
                        queue.append(node)
                        newNode = UndirectedGraphNode(node.label)
                        resultNode.neighbors.append(newNode)
                        resultQueue.append(newNode)
        return solutionNode
