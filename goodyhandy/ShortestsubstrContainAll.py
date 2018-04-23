from collections import defaultdict
import heapq

def mergeSortedLst(lsts):
    tupleLsts = []
    for i, l in enumerate(lsts):
        tupleLsts.append(map(lambda x: (x, i), l))
    print tupleLsts
    heap = []
    for l in tupleLsts:
        heapq.heappush(heap, l.pop(0))
    heapMin = heap[0]
    heapMax = max(heap)
    minWindowSize = heapMax[0] - heapMin[0]
    minWindowLeft, minWindowRight = heapMax[0], heapMin[0]
    while len(heap) == len(lsts):
        currentMin, nextInLst = heapq.heappop(heap)
        if tupleLsts[nextInLst]:
            nextTuple = tupleLsts[nextInLst].pop(0)
            heapq.heappush(heap, nextTuple)
            heapMin = heap[0]
            heapMax = max(heapMax, nextTuple)
            if heapMax[0] - heapMin[0] < minWindowSize:
                minWindowLeft, minWindowRight = heapMin[0], heapMax[0]
    print minWindowLeft, minWindowRight
    return minWindowLeft, minWindowRight
        
        
    
def shortestSub(text, wordSet):
    wordDict = defaultdict(list)
    for w in wordSet:
        for i in xrange(0, len(text)):
            if text[i:].startswith(w):
                wordDict[w].append(i)
    lists = w.values()
    leftWindow, rightWindow = mergeSortedLst(lists)
    return leftWindow, rightWindow

lsts = [[1,2,5],[3,9,10]]
mergeSortedLst(lsts)
