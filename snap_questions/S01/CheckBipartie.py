def buildGraph(pairs):
    from collections import defaultdict
    graph = defaultdict(set)
    for a, b in pairs:
        graph[a].add(b)
        graph[b].add(a)
    return graph

def checkBipartie(vertex, graph, color , setA, setB):
    child = graph[vertex]
    nextColor = None
    wrongColorSet = None 
    if color == "A":
        setA.add(vertex)
        nextColor = "B"; wrongColorSet = setA 
    else:
        setB.add(vertex)
        nextColor = "A"; wrongColorSet = setB
    for c in child:
        if c in wrongColorSet: return False
        if c not in setA and c not in setB:
            if not checkBipartie(c, graph, nextColor, setA, setB): return False
    return True

def checkAllPairs(pairs):
    graph = buildGraph(pairs)
    setA = set() ; setB = set()
    for v in graph.keys():
        if v not in setA and v not in setB:
            if not checkBipartie(v, graph, "A", setA, setB): 
                return False
    return True

#test:
print checkAllPairs([("A","B"), ("A","C"),("E","F"),("B","C")])     
print checkAllPairs([("A","B"), ("A","C"),("E","C"),("B","E")])
