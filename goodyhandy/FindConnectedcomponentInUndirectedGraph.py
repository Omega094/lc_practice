# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class unionSet(object):
    def __init__(self, nodes):
        self.ancestors = {n.label: n.label for n in nodes}
    
    def compressFind(self, nodeLabel):
        parent = self.ancestors[nodeLabel]
        if parent == nodeLabel:
            return parent
        else:
            parent = self.compressFind(parent)
            self.ancestors[nodeLabel] = parent
            return parent
    
    #Union the ancestors on two node
    def union(self, n1, n2):
        p1 = self.compressFind(n1)
        p2 = self.compressFind(n2)
        self.ancestors[p2] = p1
        return
    

class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        union_set = unionSet(nodes)
        for node in nodes:
            for child in node.neighbors:
                union_set.union(child.label, node.label)
        from collections import defaultdict
        outPut = defaultdict(set)
        for node in nodes:
            ancestor = union_set.compressFind(node.label)
            outPut[ancestor].add(node.label)
        result = []
        for components in outPut.values() :
            result.append(sorted(list(components)))
        return result
        
        
        
        
        
        
