class Solution(object):

    def dfsHelper(self, x, y , matrix, visitedDict, visited):
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        if (x, y) in visited: return visitedDict[(x,y)]
        visited.add((x,y))
        currentSet = set()
        currentSet.add(visitedDict[(x,y)])
        #print x, y
        for dx , dy in directions:
            newX, newY = x+dx, y + dy
            if   0<= newX < self.width and 0<= newY < self.height and matrix[newY][newX] <= matrix[y][x]:
                currentSet.add(self.dfsHelper(newX, newY , matrix, visitedDict, visited))
        currentSet.discard(0)
        if len(currentSet) == 0: return 0
        #print currentSet
        canGo = 0
        if len(currentSet) >= 2 or 3 in currentSet: 
            canGo = 3
            self.solution.append([y,x])
        else:
            currentSet.discard(3)
            canGo = currentSet.pop()
        visitedDict[(x,y)] = canGo
        return canGo
        
            
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        from collections import defaultdict
        visitedDict = defaultdict(int)
        width = len(matrix[0])
        height = len(matrix)
        self.width = width; self.height = height
        table = [ [ [0,0] for _ in xrange(width)] for _ in xrange(height)]
        for x in xrange(width):
            for y in xrange(height):
                if y == 0 or x == 0:
                    visitedDict[(x, y)] = 1
                elif x == width-1 or y == height -1 :
                    visitedDict[(x, y)] = 2
        visitedDict[(0, height-1)] = 3; visitedDict[(width-1, 0)] = 3
        
        visited = set()
        self.solution = []
        self.solution.append([height-1,0]); self.solution.append([0,width-1])
        #visited.add(( 0, height-1)); visited.add((width-1, 0))
        #print self.solution
        for y in xrange(0, height):
            for x in xrange(0, width):
                self.dfsHelper(x, y, matrix, visitedDict, visited)
        solution = set(map(tuple, self.solution))
        return list(solution)
