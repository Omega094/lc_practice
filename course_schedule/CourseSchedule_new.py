class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        courseDegree = collections.defaultdict(int)
        prerequeToTarget = collections.defaultdict(set)
        for p in prerequisites:
            prereque = p[1] 
            target = p[0]
            if target in prerequeToTarget[prereque]:
                continue
            courseDegree[target] += 1
            prerequeToTarget[prereque].add(target)
        #print courseDegree
        #print prerequeToTarget
        #Now starts the topological sort
        from collections import deque
        queue = collections.deque()
        for c in xrange(numCourses):
            if courseDegree[c] == 0:
                queue.append(c)
        k = 0
        while queue:
            current = queue.popleft()
            k += 1
            print current
            for c in prerequeToTarget[current]:
                courseDegree[c] -= 1
                if courseDegree[c] == 0:
                    queue.append(c)
        return k == numCourses
