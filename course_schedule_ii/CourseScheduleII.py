class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        courseDegrees = [0]*numCourses
        prerequToTargets = [[] for _ in xrange(numCourses)]
        result = []
        for pair in prerequisites:
            targetCourse = pair[0]
            prerequCourse = pair[1]
            courseDegrees[targetCourse] += 1
            prerequToTargets[prerequCourse].append(targetCourse)
        from collections import deque
        dQueue = deque()
        #Put nodes with degree 0 into the queue, then do a BFS
        for i, degree in enumerate(courseDegrees):
            if degree == 0:
                dQueue.append(i)
        while dQueue:
            currentCourse = dQueue.popleft()
            result.append(currentCourse)     
            for targetCourse in prerequToTargets[currentCourse]:
                courseDegrees[targetCourse] -= 1
                if courseDegrees[targetCourse] == 0:
                    dQueue.append(targetCourse)
        if len(result) != numCourses:
            return []
        return result

#test
if __name__ == "__main__":
    sol = Solution()
    courses = [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
    print sol.findOrder(10, courses)
